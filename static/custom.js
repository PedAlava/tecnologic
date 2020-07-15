
var contador=0;
function submit_message(message) {
    contador++;
        $.post( "/send_message", {message: message,id:contador}, handle_response);
      
        function handle_response(data) {

          // append the bot repsonse to the div
          $('.chat-container').append(`
          <div class="chat-message col-md-12 offset-md-7 bot-message">
                    ${data.message}
                </div>
          `)
          
          // remove the loading indicator
          $( "#loading" ).remove();
          //ci = int(data.id)
          //contador = ci
        
        }
        
}   
var i 
var n 
$('#target').on('submit', function(e){
    e.preventDefault();
    const input_message = $('#input_message').val()
        
    if (!input_message) {
      return
    }
    $('.chat-container').append(`
        <div class="chat-message col-md-12 human-message">
            ${input_message}
        </div>
    `)
    // loading 
    $('.chat-container').append(`
        <div class="chat-message text-center col-md-2 offset-md-10 bot-message" id="loading">
            <b>...</b>
        </div>
    `)
    $('.chat-container').append(`
        <div class="chat-message text-center col-md-2 offset-md-10 " >
           
        </div>
    `)
    // clear the text input 
    $('#input_message').val('')
    
    // send the message
    submit_message(input_message)
        
});




