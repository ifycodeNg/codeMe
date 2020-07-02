 function load(){
                let btn=document.getElementById("submit")

                let newPost=document.getElementById("matchList")
                let obj={
                    email:document.getElementById("email"),
                    phone:document.getElementById("phone"),
                    fullname:document.getElementById("fullname"),
                    message:document.getElementById("message")
                        }

                         let requestObj="email="+obj.email.value +"&phone="+obj.phone.value+"&fullname="+obj.fullname.value+"&message="+obj.message.value

                           let xhr=new XMLHttpRequest()
                        console.log(xhr.readyState)

                        xhr.onload=()=>{
                            obj.email.value="";
                            obj.phone.value="";
                            obj.message.value="";
                            obj.fullname.value="";
                            let res=JSON.parse(xhr.responseText)

                            newPost.innerHTML=`<h6> ${res.response} </h6>`

                        }

                        xhr.open("get","/message",true);

                        xhr.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
                        xhr.setRequestHeader("X-CSRFToken","{% csrf_token %}");

                        xhr.send(
                      requestObj
                        )

                      }


