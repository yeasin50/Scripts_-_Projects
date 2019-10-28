const btn = document.querySelector('.talk');
const content = document.querySelector('.content')

// creating for output msg

const greetings = ['Im good, how are you',
'Good but little busy',
"yea fine"];

const weather = [
    'Cool ','Romatic weather ','hot'
]


try{
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();


    recognition.onstart = function(){
        console.log("Voice is activited.  ");
    }

    recognition.onresult  = function(event){
        console.log(event);

        const current = event.resultIndex;
        const transcript = event.results[current][0].transcript;
        content.textContent = transcript;
        console.log(transcript);

        readOutloud(transcript);
    }

    btn.addEventListener('click', () =>{
        recognition.start();
    });

    // this will for output
    function readOutloud(message){
    
        const speech = new SpeechSynthesisUtterance();
       
       var finnalText = "can not understand";
        // setting condition for msg
       
            if (message.includes("how are you")){
                
                finnalText = greetings[Math.floor(Math.random() * greetings.length)];
                
            }
            if (message.includes('weather')){
                finnalText = weather[Math.floor(Math.random() * weather.length)];
            }
        speech.text = finnalText;
        speech.volume = 1;
        speech.rate =1;
        speech.pitch =1;
        window.speechSynthesis.speak(speech);

    }

}catch(e){
    console.log("Browser doesnt support")
}