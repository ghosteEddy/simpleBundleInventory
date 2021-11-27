function getElement(selectorType, text){
    if (selectorType === 'id'){
        return document.getElementById(text)
    }
}

function queryEle(selector){
    return document.querySelector(selector)
}

function sleep(ms){
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function postData(endpoint, body){
    response = await fetch(endpoint, {
        method: "POST",
        headers: {"X-CSRFToken": document.getElementsByName('csrfmiddlewaretoken')[0].value},
        body: JSON.stringify(body)
    }).then(data => data.json())
    return response
}

function getCurrentUrl(){return window.location.href.split("?")[0]}

function checkInputLength(element, targetLength, isGreaterOrEqualto=true){
    if (isGreaterOrEqualto) {
        return (element.value.length >= targetLength)
    }
    else{
        return (element.value.length <= targetLength)
    }
}

function setText(ele, text){
    queryEle(ele).innertext = text
}

function setValue(ele, value){
    queryEle(ele).value = value
}