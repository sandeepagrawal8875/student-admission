// ______________Only JavaScript _______________//

// <<<<<<<<<<<<<<LIVe Priview of Photo>>>>>>>>>>>>>>
let photoinput= document.getElementById("id_photo");
let photoimg = document.getElementById("priviewphoto");
photoinput.addEventListener("change",function(){
    const file = this.files[0];
    if(file){
        const reader = new FileReader();
        reader.addEventListener("load",function(){
            photoimg.setAttribute("src",this.result)
        })
        reader.readAsDataURL(file);
    }
})

// <<<<<<<<<<<<<<< LIVe Priview of  ID >>>>>>>>>>>>>>
let IDinput=document.getElementById("id_id_proof");
let IDimg=document.getElementById("priviewID");
IDinput.addEventListener("change",function(){
    const file =this.files[0];
    if(file)
    {
        const reader=new FileReader();
        reader.addEventListener("load",function()
        {
            IDimg.setAttribute("src",this.result);
        })
        reader.readAsDataURL(file);
    }
})

// <<<<<<<<<<<<<<<< LIVe Priview of Character Certificate >>>>>>>>>>>>>>>>
let CastCertiinput=document.getElementById("id_caste_certificate");
let CastCertiimg=document.getElementById("priviewCastCerti");
CastCertiinput.addEventListener("change",function(){
    const file =this.files[0];
    if(file)
    {
        const reader=new FileReader();
        reader.addEventListener("load",function()
        {
            CastCertiimg.setAttribute("src",this.result);
        })
        reader.readAsDataURL(file);
    }
})

// <<<<<<<<<<<<<<<< LIVe Priview of Domicile Certificate >>>>>>>>>>>>>>>>
let Domicileinput=document.getElementById("id_domicile");
let Domicileimg=document.getElementById("priviewDomicile");
Domicileinput.addEventListener("change",function(){
    const file =this.files[0];
    if(file)
    {
        const reader=new FileReader();
        reader.addEventListener("load",function()
        {
            Domicileimg.setAttribute("src",this.result);
        })
        reader.readAsDataURL(file);
    }
})

// <<<<<<<<<<<<<<<< LIVe Priview of TC >>>>>>>>>>>>>>>>id_character_certificate
let TCinput=document.getElementById("id_transfer_certificate");
let TCimg=document.getElementById("priviewTC");
TCinput.addEventListener("change",function(){
    const file =this.files[0];
    if(file)
    {
        const reader=new FileReader();
        reader.addEventListener("load",function()
        {
            TCimg.setAttribute("src",this.result);
        })
        reader.readAsDataURL(file);
    }
})


// <<<<<<<<<<<<<<<< LIVe Priview of Character Certificate >>>>>>>>>>>>>>>>
let CharacterCertiinput=document.getElementById("id_character_certificate");
let CharacterCertiimg=document.getElementById("priviewCharacterCerti");
CharacterCertiinput.addEventListener("change",function(){
    const file =this.files[0];
    if(file)
    {
        const reader=new FileReader();
        reader.addEventListener("load",function()
        {
            CharacterCertiimg.setAttribute("src",this.result);
        })
        reader.readAsDataURL(file);
    }
})


// <<<<<<<<<< Priview Over >>>>>>>>>>

// <<<<<<<<<< Contact Details/Populating States form json file  >>>>>>>> 

// <<<<<<<<<<< created --select-- as first option in <select>tag  >>>>>>>>>>>>>
let stateinput=document.getElementById("id_state");
let state_option=document.createElement("option");
state_option.text ="--select--";
stateinput.add(state_option);
    // ----------------

    // <<<<<<<<<<< created --select-- as first option in <city> tag >>>>>>>>>>>>>
let cityinput=document.getElementById("id_city");
let city_option=document.createElement("option");
city_option.text ="--select--";
cityinput.add(city_option);
    // ---------------

    // <<<<<<<<<<< created --select-- as first option in <pstate> tag >>>>>>>>>>>>
let pstateinput=document.getElementById("id_permanent_state");
let pstate_option=document.createElement("option");
pstate_option.text ="--select--";
pstateinput.add(pstate_option);
    // --------------

    // <<<<<<<<<<< created --select-- as first option in <city>tag 
 let pcityinput=document.getElementById("id_permanent_city");
 let pcity_option=document.createElement("option");
 pcity_option.text ="--select--";
 pcityinput.add(pcity_option);
    // ---------------

// <<<<<<<<<<<< POp States form Json fle using AJAX >>>>>>>>>>>>>
const xhr=new XMLHttpRequest()
xhr.open('GET','jsoncall',true);
xhr.onload=function()
{
    if(this.status===200)
    {
        let state=JSON.parse(this.responseText);
        for(let s in state.states)
        {
            // <<<<< Populating states for Curret address >>>>
            let option=document.createElement("option");
            option.text =state.states[s].state;
            option.value=state.states[s].state;
            stateinput.add(option);
            // <<<<< Populating states for Permanent  address >>>>>
            let p_option=document.createElement("option");
            p_option.text =state.states[s].state;
            p_option.value=state.states[s].state;
            pstateinput.add(p_option);
        }
    }
    else
    {
        console.log("some error occurerd");
    }
}
xhr.send()
// ----------------
 
// <<<<<<<<<<< Populating City  According to Selected State >>>>>>>>>>>
stateinput.addEventListener('change',function(){
   
    // <<<<<<<< To remove the privious option selected >>>>>>>>
    document.getElementById("id_city").innerHTML=null;
    
    // ------

    let getstate=document.getElementById("id_state").value;
    const xhr2=new XMLHttpRequest()
    xhr2.open('GET','jsoncall',true);
    xhr2.onload=function()
    {
        if(this.status===200)
        {
            let state=JSON.parse(this.responseText);
 
            for(let s in state.states)
            {
                 if(state.states[s].state==getstate)
                {
                    let citys=state.states[s].districts;
                    for(let count in citys )
                    {
                        let city_option=document.createElement("option");
                        city_option.text =citys[count];
                        city_option.value=citys[count];
                        cityinput.add(city_option);
                    }
                }
            }
        }
        else
        {
            console.log("some error occurerd");
        }
    }
    xhr2.send()
})
// --------

// <<<<<<<<<<< Populating P_City  According to Selected P_State>>>>>>>>>>>
pstateinput.addEventListener('change',function(){

    // <<<<<<<< To remove the privious option selected >>>>>>>>
    document.getElementById("id_permanent_city").innerHTML=null;
    // ------

    let getpstate=document.getElementById("id_permanent_state").value;
    const xhr2=new XMLHttpRequest()
    xhr2.open('GET','jsoncall',true);
    xhr2.onload=function()
    {
        if(this.status===200)
        {
            let state=JSON.parse(this.responseText);
 
            for(let s in state.states)
            {
                 if(state.states[s].state==getpstate)
                {
                    let citys=state.states[s].districts;
                    for(let count in citys )
                    {
                        let pcity_option=document.createElement("option");
                        pcity_option.text =citys[count];
                        pcity_option.value=citys[count];
                        pcityinput.add(pcity_option);
                    }
                }
            }
        }
        else
        {
            console.log("some error occurerd");
        }
    }
    xhr2.send()
})
// -----------------

// <<<<<<<<<<<<<< Address CheckBox >>>>>>>>>>>>
let checkBox=document.getElementById("checkb");
checkBox.addEventListener('click',function(){
    if(checkBox.checked==true)
    {
        // <<<<<<<< To remove the privious option selected >>>>>>>>
        document.getElementById("id_permanent_city").innerHTML=null;
        document.getElementById("id_permanent_state").innerHTML=null;
        // ------

        // <<<<<<<<<<<<<< all Current Address fields >>>>>>>>>>>>>>
        let addr=document.getElementById("id_current_addr").value;
        let addr2=document.getElementById("id_current_addr2").value;
        let gstate=document.getElementById("id_state").value;
        let city=document.getElementById("id_city").value;
        let pin=document.getElementById("id_pincode").value;
 
        if(addr !== "" || addr2!== "")
        {
            // <<<<<<<<<<<<<<<<< all Permanent Address Fields >>>>>>>>>>>>>>>
            document.getElementById("id_permanent_addr").value=addr;
            document.getElementById("id_permanent_addr2").value=addr2;
            document.getElementById("id_permanent_pincode").value=pin;
          
            // <<<<<<<<<<< POpulating State (Which user has Selected in Current Address) >>>>>>>>>>>
            let pstate=document.getElementById("id_permanent_state");
            let pstate_option=document.createElement("option");
            pstate_option.text=gstate;
            pstate.add(pstate_option);

            // <<<<<<<<<<<<< Populating City (Which user has Selected in Current Address) >>>>>>>>>>>>>
            let pcity=document.getElementById("id_permanent_city");
            let pcity_option=document.createElement("option");
            pcity_option.text=city;
            pcity.add(pcity_option);
            console.log("this not equal to if is called")
        }
        else
        {
            alert("please provide all fields of 'Current address' details");
        }
    }
})

//______________________________________//



