// use utils.js
async function deleteItem(item_id){
    confirmation = window.confirm('Delete?')
    console.log(item_id)
    console.log(confirmation)
    if (confirmation == true){
        response = await postData(window.location.href + "/delete/" + item_id, {'item_id' : item_id})
        if (response.result === 0){
            window.location.replace(window.location.href)
        }
        else {
            window.alert('Something Wrong Error: ' + response.result)
        }
    }
}