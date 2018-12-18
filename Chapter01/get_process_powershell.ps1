Get-Process `
| Where-Object {$_.company -like ‘*Microsoft*’}`
| Where-Object {($_.ProcessName -like ‘*System*’) -or ($_.ProcessName -like ‘*powershell*’)}`
| Format-Table ProcessName, Company -auto