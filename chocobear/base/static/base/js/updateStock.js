// use utils.js
async function updateItem(item_id, item_name, flowType){
    let buttonEle = document.getElementById(item_id).querySelector('button')
    buttonEle.disabled = true
    let form = document.getElementById(item_id)
    let update_amountEle = form.querySelector('input[name="update_amount"]')
    let update_amount = update_amountEle.value
    let form2 = document.getElementById(item_id)
    let update_remarkEle = form2.querySelector('input[name="update_remark"]')
    let update_remark = update_remarkEle.value
    if (update_amount > 0){
        if (flowType === 'manualIn'){
            flowType = 'MANUAL'            
        }
        else if(flowType === 'manualOut'){
            flowType = 'MANUAL'
            update_amount = update_amount * -1
            console.log(update_amount)
        }
        response = await postData("/updateInventory", {'item_id' : item_id, 'flowType' : flowType, 'update_amount' : update_amount, 'update_remark' : update_remark})
        if (response.result === 0){
            window.alert('Done. Update ' + item_name + ' amount : ' + update_amount)
            window.location.replace(window.location.href)
            console.log('success')
        }
        else {
            // window.alert('Something Wrong Error: ' + response.result)
        }
    } else {
        window.alert('Please put in positive number!!!')
        buttonEle.disabled = false
    }
}