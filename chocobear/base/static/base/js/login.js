// *** importing utils.js ***

// track usrname and pw input
(() => {
    let isUsrPass = false
    let isPwdPass = false
    
    let usrEle = queryEle("#username")
    let pwdEle = queryEle("#password")

    async function validateForLoginButton(){
        await sleep(10)
        isUsrPass = checkInputLength(usrEle, 5)
        isPwdPass = checkInputLength(pwdEle, 5)
        if (isUsrPass && isPwdPass){
            queryEle("#lgin-btn").disabled = false
        }
        else{
            queryEle("#lgin-btn").disabled = true
        }
    }
    // validate first time during page load then apply event tracker
    validateForLoginButton()
    usrEle.onkeydown = () => {
        validateForLoginButton()
    }
    pwdEle.onkeydown = () => {
        validateForLoginButton()
    }
})()