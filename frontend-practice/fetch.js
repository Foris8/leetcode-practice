
async function submitForm(
    username,
    email,
    password,
    passwordConfirm,
){
    try{
        const response = await fetch("url",{
            method: 'POST',
            header: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username,
                email,
                password
            })
        })
        const {messgae} = await response.json();

    }catch{
        alert("error")
    }
}