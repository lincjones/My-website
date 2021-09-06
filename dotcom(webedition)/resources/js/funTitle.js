var i=0;
setInterval(function(){
    var titles=['Hi everyone',
    'Salut tout le monde',
    'Cao svima',
    "BOOLEAN",
    "True",
    "False",
    "jkhkdsfhkjdshkfjhdskjhf",
    "😀_______",
    "😀______🐲",
    "😏_____🐲",
    "😐____🐲",
    "😑___🐲",
    "😩__🐲",
    "🔥",
    "👻",
    "title-'Im clocking out'",
    "-",
    "-",
    "-",
    "-",
    "-",
    "-",
    "Im baaack",
    "Im about to check your search history!"];
    if(i===titles.length) {
        i=0;
    }
    document.title = titles[i];
    i++;
}, 3000);