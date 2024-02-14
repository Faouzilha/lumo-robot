*** Settings ***
Library  SeleniumLibrary
Test Setup    Open Browser    https://magento.softwaretestingboard.com/?ref=hackernoon.com    chrome
Test Teardown    Close Browser

*** Variables ***
${BASE_URL}    	https://www.google.com/ 
${URL}   https://magento.softwaretestingboard.com/?ref=hackernoon.com
${NEW_ACCOUNT_URL}    https://magento.softwaretestingboard.com/customer/account/create/
${USER_FIRST_NAME}    Sonny
${USER_LAST_NAME}     Melissa
${USERNAME}   sonny@exemple.com
${PASSWORD}   Sonny1306.

*** Test Cases ***
Create  
    Maximize Browser Window
    Open Browser    ${BASE_URL}    chrome
    Go To    ${URL}
    Click Link    Create an Account
    Go To    ${NEW_ACCOUNT_URL}
    Input Text    id=firstname    ${USER_FIRST_NAME}
    Input Text    id=lastname     ${USER_LAST_NAME}
    Input Text    id=email_address    ${USER_NAME}
    Input Text    id=password    ${PASSWORD}
    Input Text    id=password-confirmation    ${PASSWORD}
    Click Button    //form[@id='form-validate']/div/div/button/span/font/font
    Go To    https://magento.softwaretestingboard.com/customer/account/
    Click Button    //button[@type='button']
    Click Element    xpath=(.//*[normalize-space(text()) and normalize-space(.)=concat('Ma liste d', "'", 'envies')])[1]/following::font[2]
    Go To    https://magento.softwaretestingboard.com/
    Login    ${USERNAME}    ${PASSWORD}
    Logout

*** Keywords ***
Login
    [Documentation]    Test formule connexion 
    [Arguments]     ${EMAIL}    ${PASSWORD}
    Go To    ${URL}
    Input Text    id=email    ${EMAIL}
    Input Text    id=pass    ${PASSWORD}
    Click Element    xpath=//ul[@class='level1 submenu ui-menu ui-widget ui-widget-content ui-corner-all expanded']/li[@class='level2 nav-3-1-1 category-item first ui-menu-item']/a/span[1]


Logout   
    [Documentation]    Test de deconnexion
    Wait Until Page Contains    xpath=//div[@class='panel header'][1]/ul[@class='header links']    timeout=10s     
    Click Button    xpath=//div[@class='panel header'][1]/ul[@class='header links'][1]/li[@class='customer-welcome']/span/button   
    Click Element  xpath=//div[@class='customer-menu']/ul/li[@class='authorization-link']/a  
#[Teardown]    Close Browser
