*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  kalle  kalle1234
    Output Should Contain  New user registered 
    

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  joku  joku1234
    Input New Command
    Input Credentials  joku  joku1234
    Output Should Contain  User with username joku already exists


Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  jo  joku1234adadada
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  joku  joku123
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  joku  jokuvaandadasdadasda
    Output Should Contain  Password containing only letters

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  joku  joku1234
    Run Application