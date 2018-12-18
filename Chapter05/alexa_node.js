NODE.JS code hosted as Lambda function in AWS


const Alexa = require('ask-sdk-core');
const LaunchHandler = {
    canHandle(handlerInput) {
    return handlerInput.requestEnvelope.request.type === 'LaunchRequest';
  },
  handle(handlerInput) {
      var speechText = "Welcome to Splunk Center!, What would you like to do today?"
      return handlerInput.responseBuilder
      .speak(speechText)
      .withShouldEndSession(false)
      .getResponse();
  }
};

const splunkintentHandler = {
    canHandle(handlerInput) {
    return handlerInput.requestEnvelope.request.type === 'IntentRequest' && (handlerInput.requestEnvelope.request.intent.name === 'splunkintent');
  },
 async handle(handlerInput) {
      var inp_status = handlerInput.requestEnvelope.request.intent.slots.status.value;
      var outputSpeech = "";
      var url = 'http://13.59.112.54/splunk/runquery';
      var data = ''
      if (inp_status == "up")
      data = {"query":"search%20index%3D%22main%22%20earliest%3D0%20%7C%20where%20interface_name%3D%22Loopback45%22%20%7C%20dedup%20interface_name%2Crouter_name%20%7C%20where%20interface_status%3D%22up%22%20%7C%20stats%20values%28interface_name%29%20values%28interface_status%29%20by%20router_name%20%7C%20table%20router_name"};
      else if (inp_status == "down")
      data = {"query":"search%20index%3D%22main%22%20earliest%3D0%20%7C%20where%20interface_name%3D%22Loopback45%22%20%7C%20dedup%20interface_name%2Crouter_name%20%7C%20where%20interface_status%21%3D%22up%22%20%7C%20stats%20values%28interface_name%29%20values%28interface_status%29%20by%20router_name%20%7C%20table%20router_name"};
      var res;
      var router_array =[];
      await POSTdata(url,data)
      .then((response) => {
      res = JSON.parse(response);
      console.log(res);
      var arr_len = res.result.length;
      for (var i=0;i<arr_len;i++)
      {
        console.log (res.result[i].router_name);
        router_array.push(res.result[i].router_name);
      }
      })
      .catch((err) => {
        outputSpeech = 'Error'+err.message;
      });
       var count = router_array.length;
       for (let i = 0; i < count; i++) {
          if (i === 0) {
            //first record
            outputSpeech = outputSpeech + 'Routers with status as '+ inp_status +" are: " + router_array[i] +','
          } else if (i === count - 1) {
            //last record
            outputSpeech = outputSpeech + 'and ' + router_array[i] +'.'
          } else {
            //middle record(s)
            outputSpeech = outputSpeech + router_array[i] + ', '
          }
        }
        if (count == 1)
        {
          outputSpeech = router_array[0]+' is identified with status as '+ inp_status +'.'
        }
      return handlerInput.responseBuilder
      .speak(outputSpeech)
      .withShouldEndSession(false)
      .getResponse();
  }
};

const ErrorHandler = {
  canHandle() {
    return true;
  },
  handle(handlerInput, error) {
    console.log(`Error handled: ${error.message}`);

    return handlerInput.responseBuilder
      .speak('Sorry, I can\'t understand the command. Please say again.')
      .reprompt('Sorry, I can\'t understand the command. Please say again.')
      .getResponse();
  },
};
const POSTdata = function (url,body) {
  return new Promise((resolve, reject) => {
    const request = require('request');

request.post({
    headers: {"Accept":"application/json","Content-Type":"application/json"},
    url: url,
    method: 'POST',
    body: JSON.stringify(body)
  }, function(error, response, body){
    resolve(body);
  });
  })
};
const skillBuilder = Alexa.SkillBuilders.custom();

exports.handler = skillBuilder
  .addRequestHandlers(
    LaunchHandler,
    splunkintentHandler
  )
  .addErrorHandlers(ErrorHandler)
  .lambda();
