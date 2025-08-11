let chat_id = 0
function send_message() {
    $('#input').val('')
    $.ajax({
        url: '/send_message',
        type: 'post',
        contentType: 'application/json',
        data: JSON.stringify({
            prompt: $('#input').val(),
            status: 'auth',
            chat_id: chat_id
        }),
        success: function (result) {
            const data = JSON.parse(result)
            console.log(data)
            chat_block.innerHTML = ''
            chat_id = data['chat_id']
            let messages = data['messages']
            for (index in messages) {
                message_frame = document.createElement('div')
                console.log(messages[index].content)
                message_frame.textContent = messages[index].content
                chat_block.appendChild(message_frame)
            }
        }
    })

}
$('.input_button').click(send_message)

$('#input').on('keydown', function (event) {
    if (event.key == 'Enter') {
        send_message()
    }
    
})

const chat_block = document.getElementById('chat')

$('.chat_btn').click(function () {
    chat_id = parseInt($(this).attr('chat_id'))
    $.ajax({
        url: '/open_chat',
        type: 'post',
        contentType: 'application/json',
        data: JSON.stringify({
            'chat_id': chat_id
        }),
        success: function (result) {
            const data = JSON.parse(result)
            chat_block.innerHTML = ''
            for (index in data) {
                message_frame = document.createElement('div')
                console.log(data[index].content)
                message_frame.textContent = data[index].content
                chat_block.appendChild(message_frame)
            }
        }
    })
})
