const send_button = document.getElementById('send_message')
const input_message = document.getElementById('input_message')
const messages = document.querySelector('.messages')
let list_messages = []
function send_message() {
    let all_messages = messages.querySelectorAll('div')
    all_messages.forEach((message, index) => {
        if (message.classList.contains('message_from')) {
            list_messages.push({
                'content': message.textContent,
                'role': 'user'
            }
            )
        }
        else {
            list_messages.push({
                'content': message.textContent,
                'role': 'assistant'
            }
            )
        }
    })
    if (input_message.value.trim() != '') {
        let prompt = input_message.value.trim()
        let message_frame = document.createElement('div')
        message_frame.classList.add('message_from')
        let message_text = document.createElement('h4')
        message_text.textContent = prompt
        message_frame.appendChild(message_text)
        messages.appendChild(message_frame)
        fetch('/send_message', {
            method: 'POST',
            body: JSON.stringify({ prompt: prompt, messages: list_messages, status: 'anon'})
        })
            .then(response => {
                return response.json()
            })
            .then(data => {
                let answer = data.choices[0].message.content
                let message_frame = document.createElement('div')
                let message_text = document.createElement('h4')
                let copy_svg = document.createElement('img')
                copy_svg.src = '/static/media/copy.svg'
                copy_svg.onclick = function () {
                    navigator.clipboard.writeText(message_text.textContent)
                }
                message_text.textContent = answer
                message_frame.appendChild(message_text)
                message_frame.appendChild(copy_svg)
                messages.appendChild(message_frame)
            })
    }
    input_message.value = ''
}
send_button.addEventListener('click', () => {
    send_message()
})

input_message.addEventListener('keydown', (event) => {
    if (event.key == 'Enter') {
        send_message()
    }
})