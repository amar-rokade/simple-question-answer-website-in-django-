function openNav() {
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
  }
  
  function closeNav() {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
  }

function  Change_content(response){
  
    $(".mainpage_replace").html(response)
}
window.addEventListener('popstate', e =>{
  if(e.state.response){
    Change_content(e.state.response);
  }
})
//============user search=============
function User_search(query){
  if (query){
    $.ajax({
      type: 'POST',
      url: "search/result/",
      dataType: 'json', 
      data: { csrfmiddlewaretoken: $(".csrf_value").val(),query:query},
  })
  .done(function(response){
      if (response.count != 0){
          $('#user_search_result').html(response.rendered_html);
          $('#user_search_result').show();
      }
      else{
          $('#user_search_result').hide();
      }
  });
  }
  
}
  //content ajax replacement with profile 
function profile(id){
  if(id){
    $(".mainpage_replace").fadeOut()
  $("#main_spinner").show();
  $.ajax( 
    { 
      type:"POST", 
      url: "Profile/ajax/view_profile/", 
      data:{ csrfmiddlewaretoken: $(".csrf_value").val(), profile_id: id },
      dataType: 'json', 
    })
    .done(function(response){
     $(".mainpage_replace").html(response)
     window.history.pushState({response}, 'profile','Profile/');
     $("#main_spinner").hide();
     $(".mainpage_replace").fadeIn('slow')
    });
  }
  
}

//content ajax replacement with profile 
function home(){
  $(".mainpage_replace").fadeOut()
  $("#main_spinner").show();
  $.ajax( 
    { 
     type:"POST", 
     url: "home_page/ajax/home_page_view/", 
     data:{ csrfmiddlewaretoken: $(".csrf_value").val() },
     dataType: 'json', 
   })
   .done(function(response){
    $(".mainpage_replace").html(response)
    window.history.pushState({response}, 'home','home_page/');
    $("#main_spinner").hide();
    $(".mainpage_replace").fadeIn('slow')
   });
}

//content ajax replacement with profile 
function blog(){
  $(".mainpage_replace").fadeOut()
  $("#main_spinner").show();
  $.ajax( 
    { 
     type:"POST", 
     url: "blogs/blog_list/", 
     data:{ csrfmiddlewaretoken: $(".csrf_value").val() },
     dataType: 'json', 
   })
   .done(function(response){
    $(".mainpage_replace").html(response)
    window.history.pushState({response}, 'blogs','blogs/');
    $("#main_spinner").hide();
    $(".mainpage_replace").fadeIn('slow')
   });
}




function Ask(){
  
  $(".mainpage_replace").fadeOut()
  $("#main_spinner").show();
  $.ajax( 
    { 
     type:"POST", 
     url: "ask_questions/asked_quetions/", 
     data:{ csrfmiddlewaretoken: $(".csrf_value").val() },
     dataType: 'json', 
   })
   .done(function(response){
    $(".mainpage_replace").html(response)
    window.history.pushState({response}, 'ask','ask_questions/');
    $("#main_spinner").hide();
    $(".mainpage_replace").fadeIn('slow')
   });
}

function Chat(){
  $(".mainpage_replace").fadeOut();
  $("#main_spinner").show();
  $.ajax( 
    { 
     type:"POST", 
     url: "message/", 
     data:{ csrfmiddlewaretoken: $(".csrf_value").val() },
     dataType: 'json', 
   })
   .done(function(response){
    $(".mainpage_replace").html(response)
    window.history.pushState({response}, 'chat','chat/');
    $("#main_spinner").hide();
    $(".mainpage_replace").fadeIn('slow')
   });
}

function notification(){
  $.ajax(   
    { 
        type:"POST", 
        url: "notifications/", 
        data:{ csrfmiddlewaretoken: $(".csrf_value").val(),
                
             },
        dataType: 'json', 
      })
      .done(function(response){
       $("#notification_count").html(response.notificationscount)
      });
}