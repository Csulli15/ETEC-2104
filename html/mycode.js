function Check(){
    let theinput = document.getElementById("birth");
    let b = theinput.value;
    theinput = document.getElementById("email");
    let e = theinput.value;
    theinput = document.getElementById("name");
    let n = theinput.value;
    theinput = document.getElementById("password");
    let p = theinput.value;
    
    //Fill-in check
    if ( p.length == 0 || b.length == 0 || e.length == 0 || n.length == 0 ) {
        alert("Please fill in all areas");
        return
    }
    
    //Time check
    let birthday = new Date(b);
    let d = birthday.getTime();
    let day = Date.now();
    if (d > day - 410248800000) {
        alert("LEAVE, CHILD");
        return
    }
    
    //Email check
    let first = e.indexOf("@");
    if (first == -1 || first == 0 || first == e.length - 1) {
        alert("Invalid Email");
        return
    }
    let second = e.indexOf("@", first + 1);
    if (second > 0) {
        alert("Invalid Email");
        return
    }
    
}
