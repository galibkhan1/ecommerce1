function validateform()
{
    x = document.forms["myform"]["email"].value;
    if(x==""){
        document.getElementById('email').placeholder ="enter your email";
        document.getElementById('email').style.border ="2px solid red";
        // document.getElementById('email').
        x = document.getElementById('valid');
        x.innerHTML = "*enter your email";
        x.style.color ="red"
        return false;
    }



}
