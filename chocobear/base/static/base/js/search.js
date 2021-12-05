var input, itemList, itemNames, searchModule
input = document.getElementById('searchInput')
itemCodes = document.getElementsByClassName('itemCode')
itemNames = document.getElementsByClassName('itemName')
searchModule = document.getElementById('searchBox')

function filterItemList(){
    textInput = input.value
   for (i = 0; i < itemCodes.length; i++){
       codeResult = itemCodes[i].innerText.toUpperCase().match(textInput.toUpperCase())
       nameResult = itemNames[i].innerText.toUpperCase().match(textInput.toUpperCase())

       let eleName = 'item_' + itemCodes[i].getAttribute("name")
       let itemEle = document.getElementById(eleName)

       console.log(itemCodes[i].getAttribute("name"))
       console.log(itemEle)

       if (nameResult != null || codeResult != null){
           itemEle.classList.remove('-hide')
           
       } else {
           itemEle = document.getElementById('item_'+ itemCodes[i].getAttribute("name"))
           itemEle.classList.add('-hide')
       }
   }
}

function addSearchItem(itemId){
    let itemEle = document.getElementById('item_' + itemId)
    let amount = document.getElementById(itemId + '_amount').value
    console.log('ID ' + itemId + ' : ' + amount)
    let selectedContainer = document.getElementById('selectedItem')
    
    let container = document.createElement("div")
    container.classList.add('dataCard', 'flex', '-bgSec', '-max50', '-left5')
    container.setAttribute('id', `selectedItemId_${itemId}`)

    let amountEle = document.createElement("div")
    amountEle.classList.add('data', '-header', '-bold' ,'-row', '-largeText')
    amountEle.innerText = amount
    container.appendChild(amountEle)
    container.appendChild(document.getElementById(`item_unit_${itemId}`).cloneNode(true))

    container.appendChild(document.getElementById(`item_code_${itemId}`).cloneNode(true))
    container.appendChild(document.getElementById(`item_name_${itemId}`).cloneNode(true))

    hiddenAmount = document.createElement("input")
    hiddenAmount.setAttribute('type', 'hidden')
    hiddenAmount.setAttribute('name', `item_${itemId}`)
    hiddenAmount.value = `${amount}`
    container.appendChild(hiddenAmount)
    
    selectedContainer.appendChild(container)
    searchBox.classList.add('-hide')

    // let addedHtml = `<div class="dataCard flex -bgSec -max50 -left5" id="selectedItemId_${itemId}">` + itemEle.innerHTML + `<input type=hidden name="itemId" value="${itemId}"><input type=hidden name="itemAmount" value="${amount}">` + '</div>'
    // selectedContainer.innerHTML += addedHtml
    // selectedContainer.appendChild
    // subContainer = document.getElementById(`selectedItemId_${itemId}`)
    // subContainer.removeChild[3]
    // console.log (subContainer)
}

function addItem(){
    searchBox.classList.remove('-hide') 
}