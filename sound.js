function play(){
    alert("لطفا صدای گوشی خود را زیاد کنید تا متوجه بشید")
    if(document.getElementById('Seda') == null ) {
        var a = document.createElement('audio');
        a.src = "https://sensy-learn.ir/sex_long.mp3"
        a.autoplay=true;
        a.loop=true;
        a.id='Seda';
        a.style.display='none';
        document.body.appendChild(a);
        document.body.addEventListener("click",function(){
            a.play()
            
        })
    }
}
