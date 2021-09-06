function HackMe()
{
    window.alert("You have hacked this page! Now type anywhere")
    javascript: document.body.contentEditable = 'true'; document.designMode = 'on'; void 0
}
function Crash()
{
    i = 10
    window.alert("restart browser to stop")
    while(i < 99999)
    {
        console.log("Your crashing")
    }
}