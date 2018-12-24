# Practical-Network-Automation-Second-Edition

<a href="https://www.packtpub.com/virtualization-and-cloud/implementing-azure-solutions-second-edition?utm_source=github&utm_medium=repository&utm_campaign=9781789343045"><img src="https://packt-type-cloud.s3.amazonaws.com/uploads/sites/3188/2018/12/9781789955651.png" alt="Practical Network Automation Second Edition" height="256px" align="right"></a>

This is the code repository for [Practical Network Automation Second Edition](https://www.packtpub.com/virtualization-and-cloud/implementing-azure-solutions-second-edition?utm_source=github&utm_medium=repository&utm_campaign=9781789343045), published by Packt.

**A beginner's guide to automating and optimizing networks using Python, Ansible and more**

## What is this book about?
Network automation is the process of efficiently automating the management and functionality of networks. Through practical use-cases and examples, this book introduces you to the popular tools such as Python, Ansible, Chef and more, that are used to automate a network.

This book covers the following exciting features:
* Get started with the fundamental concepts of network automation
* Perform intelligent data mining and remediation based on triggers
* Understand how AIOps works in operations
* Trigger automation through data factors
* Improve your data center's robustness and security through data digging
* Get access infrastructure through API Framework for chatbot and voice interactive troubleshootings
* Set up communication with SSH-based devices using Netmiko

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1789343046) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders. For example, Chapter02.

The code will look like the following:
```
index="main" earliest=0 | where interface_name="Loopback45" | dedup interface_name,router_name | where interface_status="up" | stats values(interface_name) values(interface_status) by router_name | table router_name

```

**Following is what you need for this book:**
If you are a network engineer or a DevOps professional looking for an extensive guide to help you automate and manage your network efficiently, then this book is for you. No prior experience with network automation is required to get started, however you will need some exposure to Python programming to get the most out of this book.

With the following software and hardware list you can run all code files present in the book (Chapter 1-11).
### Software and Hardware List
| Chapter | Software required | OS required |
| -------- | ------------------------------------ | ----------------------------------- |
| 1-6| PowerShell, Python, Ansible, Syslog Server, Visual Studio  | Computer with Windows, Linux or macOS |


We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://www.packtpub.com/sites/default/files/downloads/9781789955651_ColorImages.pdf).

### Related products <Paste books from the Other books you may enjoy section>
* Practical Network Scanning [[Packt]](https://www.packtpub.com/networking-and-servers/practical-network-scanning?utm_source=github&utm_medium=repository&utm_campaign=9781788839235) [[Amazon]](https://www.amazon.com/dp/1788839234)

* Practical AWS Networking [[Packt]](https://www.packtpub.com/virtualization-and-cloud/practical-aws-networking?utm_source=github&utm_medium=repository&utm_campaign=9781788398299) [[Amazon]](https://www.amazon.com/dp/1788398297)
## Get to Know the Authors
**Abhishek Ratan**
has around 16 years of technical experience in networking, automation, and various ITIL processes, and has worked in a number of roles in different organizations. As a network engineer, security engineer, automation engineer, TAC engineer, tech lead, and content writer, he has gained a wealth of experience in his career. He also has a keen interest in strategy game playing and, when he is not working on technical stuff, he is busy spending time on his strategy games. He is currently leading the automation and monitoring team, learning, and expanding his automation and Artificial Intelligence skills in the ServiceNow. His previous experience includes working for companies such as Microsoft, Symantec, and Navisite.

# Other book by the author
* [Practical Network Automation](https://www.packtpub.com/networking-and-servers/practical-network-automation?utm_source=github&utm_medium=repository&utm_campaign=9781788299466)

### Suggestions and Feedback
[Click here](https://docs.google.com/forms/d/e/1FAIpQLSdy7dATC6QmEL81FIUuymZ0Wy9vH1jHkvpY57OiMeKGqib_Ow/viewform) if you have any feedback or suggestions.

