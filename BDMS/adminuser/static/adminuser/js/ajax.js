$("#updatecontact").click(function(e){
    e.preventDefault();
    let mob=$("#mobile").val();
    let eml=$("#emailid").val();
    let csr=$("input[name='csrfmiddlewaretoken']").val();
    if(mob==""){
        $("#msg").html("<h4 class='text-warning'>Please Enter The Mobile Number</h4>");
    }
    else  if(eml==""){
        $("#msg").html("<h4 class='text-warning'>Please Enter The Email ID</h4>");
    }
    else{
        mydata={mob:mob,eml:eml,csrfmiddlewaretoken:csr};
        $.ajax({
            url:'/adminuser/newcontactdetails/',
            method:'POST',
            data:mydata,
            success:function(data){
                $("#msg").html("<h4 class='text-success'>Contact Details Successfully Updated!!!</h4>");
            }

        });
    }
})

$("#updateaboutus").click(function(e){
    e.preventDefault();
    let newabt=$("#newaboutus").val();
    let csr=$("input[name='csrfmiddlewaretoken']").val();
    if(newabt==""){
        $("#message").html("<h4 class='text-warning'>Please Enter The Details</h4>");
    }
    else{
        mydata={newabt:newabt,csrfmiddlewaretoken:csr};
        $.ajax({
            url:'/adminuser/newaboutdetails/',
            method:'POST',
            data:mydata,
            success:function(data){
                $("#message").html("<h4 class='text-success'>About Details Successfully Updated!!!</h4>");
            }

        });
    }
})





