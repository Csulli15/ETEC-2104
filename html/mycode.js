function Check(){
    let theinput = document.getElementById("birth");
    let b = theinput.value;
    theinput = document.getElementById("email");
    let e = theinput.value;
    theinput = document.getElementById("name");
    let n = theinput.value;
    theinput = document.getElementById("password");
    let p = theinput.value;
    
    good = 0;
    let temp = document.getElementsByClassName("alert")
    if (temp.length > 0){
        temp[0].parentNode.removeChild(temp[0])
    }
    let tmp = document.createElement("div");
    tmp.classList.add("alert");
    document.body.appendChild(tmp);
    
    //Fill-in check
    if ( p.length == 0 || b.length == 0 || e.length == 0 || n.length == 0 ) {
        tmp.appendChild(document.createTextNode("You have not filled out all necessary information."));
        good++
    }
    
    //Time check
    let birthday = new Date(b);
    let d = birthday.getTime();
    let day = Date.now();
    if (d > day - 410248800000) {
        tmp.appendChild(document.createTextNode(" BE GONE CHILD! "));
        good++
    }
    
    //Email check
    let first = e.indexOf("@");
    if (first == -1 || first == 0 || first == e.length - 1) {
        tmp.appendChild(document.createTextNode(" Invalid email. "));
        good++
    }
    let second = e.indexOf("@", first + 1);
    if (second > 0) {
        tmp.appendChild(document.createTextNode(" Invalid email. "));
        good++
    }

    if (good == 0){
        tmp.classList.remove("alert");
        tmp.classList.add("welcome");
        tmp.appendChild(document.createTextNode("Welcome!"))
    }
    
}
