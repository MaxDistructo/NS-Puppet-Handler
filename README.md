# NS-Puppet-Handler
NationStates Puppet Handler 

Designed to automatically answer every issue for puppet nations where all we want is for the population to increase without a care on what the nation does. 

# Usage
Copy the puppets.json.example to puppets.json and set your puppet's username and password as follows
{
  "puppet1":"password1",
  "puppet2":"password2",
  ...
  "puppetx":"passwordx"
}

If you don't want to automatically answer issues but prevent CTE, put the nation in cte.json following the cte.json.example file. Format is the exact same as puppets.json just only prevents the nation from CTEing.
{
  "puppet1":"password1",
  "puppet2":"password2",
  ...
  "puppetx":"passwordx"
}

Please also either set the following environment variables or replace the placeholder text at the top of both scripts. THIS IS REQUIRED BY NATIONSTATES API RULES, FAILIURE TO COMPLY MAY GET YOUR IP BANNED.

NS_CTE_UA="PrimaryNation Anti-CTE Script"
NS_ISSUE_UA="PrimaryNation Puppet Issue Answer Script"
