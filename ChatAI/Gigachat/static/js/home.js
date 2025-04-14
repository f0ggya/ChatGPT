const send_button = document.getElementById('send_message')
const input_message = document.getElementById('input_message')
send_button.addEventListener('click', () => {
    if (input_message.value.trim() != ''){
        let prompt = input_message.value.trim()
        fetch('/send_message', {
            method: 'POST',
            body: JSON.stringify({prompt: prompt})
        })
        .then(response => {
            console.log(response.json())
        })
    }
})