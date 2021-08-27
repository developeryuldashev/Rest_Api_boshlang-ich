console.log('realtime js working ......')
var websocket = new WebSocket( 'ws://127.0.0.1:8000/ws/real_data/');
    websocket.onmessage=function(event){
    var data=JSON.parse(event.data);
    console.log(data);
    // document.querySelector(selector: '#root').innerText=data.number;
    document.getElementById('root').innerText=data.number;
    }