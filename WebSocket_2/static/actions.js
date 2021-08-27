document.getElementById('room-name-imput').onkeyup=function(event){
    if(event.keyCode==13) {
        document.getElementById('room-name-submit').click()
        }
}
document.getElementById('room-name-submit').onclick=function(e){
    var roomname=document.getElementById('room-imput').value
    window.location.pathname('chat/${roomname}')
}

