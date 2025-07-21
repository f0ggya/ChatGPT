let chat_id = 0
function send_message() {
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
            message_text.classList.add('text_from')
            document.body.appendChild(message_frame)
        }
    })
}
$('.input_button').click(send_message)

$('#input').on('keydown', function(event){
    if (event.key == 'Enter') {
        send_message()
        $(this).val('')
    }
})

const chat_block = document.getElementById('chat')

$('.chat_btn').click(function(){
    chat_id = parseInt($(this).attr('chat_id'))
    $.ajax({
        url: '/open_chat',
        type: 'post',
        contentType: 'application/json',
        data: JSON.stringify({
            'chat_id': chat_id
        }),
        success: function (result){
            const data = JSON.parse(result)
            chat_block.innerHTML = ''
            for (index in data){
                message_frame = document.createElement('div')
                console.log(data[index].content)
                message_frame.textContent = data[index].content
                chat_block.appendChild(message_frame)
            }
        }
    })
})
