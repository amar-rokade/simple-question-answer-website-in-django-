

//my asked question
function My_asked_question(user_id){
  if (user_id){
    $(".mainpage_replace").fadeOut();
  $("#main_spinner").show();
    $.ajax(
        { 
          type:"POST", 
          url: "my_asked_quetions/", 
          data:{ csrfmiddlewaretoken: $(".csrf_value").val(),
                      user_id:user_id},
          dataType: 'json', 
        })
        .done(function(response){
          $(".mainpage_replace").html(response)
          window.history.pushState({response}, 'ask','ask_questions/my_asked_quetions/');
          $("#main_spinner").hide();
          $(".mainpage_replace").fadeIn('slow')
        });
  }
  
}

//my answers 
function  My_answers(user_id){
  if (user_id){
    $(".mainpage_replace").fadeOut();
  $("#main_spinner").show();
    $.ajax(
        { 
          type:"POST", 
          url: "ask_questions/my_answered_quetions/", 
          data:{ csrfmiddlewaretoken: $(".csrf_value").val(),
          user_id:user_id},
               dataType: 'json', 
        })
        .done(function(response){
          $(".mainpage_replace").html(response)
          window.history.pushState({response}, 'ask','ask_questions/my_answered_quetions/');
          $("#main_spinner").hide();
          $(".mainpage_replace").fadeIn('slow')
          
        });
  }
}

//question upvote
function Quetion_upvote(question_id,vote_type){
  if(question_id && vote_type){
    $.ajax( 
      { 
          type:"POST", 
          url: "/question/upvote/", 
          data:{  csrfmiddlewaretoken: $(".csrf_value").val(),
                  question_id: question_id ,vote_type:vote_type
               },
          dataType: 'json', 
        })
        .done(function(response){
          if (vote_type == "upvote"){
            if(response.is_user_voted){
              $('.question_upvote_class'+question_id).attr("src","/static/img/profile/upvoted.png")
              $('.question_downvote_class'+question_id).attr("src","/static/img/profile/downvote.png")
              }
              else{
                $('.question_upvote_class'+question_id).attr("src","/static/img/profile/upvote.png")
              }
          }
          else{
            if(response.is_user_voted){
              $('.question_downvote_class'+question_id).attr('src','/static/img/profile/downvoted.png')
              $('.question_upvote_class'+question_id).attr('src','/static/img/profile/upvote.png')
              }
              else{
                $('.question_downvote_class'+question_id).attr('src','/static/img/profile/downvote.png')
              }
          }
          $('.question_upvote_count'+question_id).html(response.upvote_count)
          $('.question_downvote_count'+question_id).html(response.downvote_count)
        });
  }

}


//Question comment form 
function Question_new_comment(question_id,method){
  //changing title of modal according to answer or question comment type
 $('ask_comment_title').html('question comment')
  //changing question id for new comment submision
  $('.question_comment_form').attr('data-catid',question_id)
  $('.question_comment_form').attr('answer_or_question','question')

  //checking type of method
  if (method == "GET"){
    $('.ask_comment_spinner').show();
    $('.question_commentlist_modal').html('')
    $("#question_comment_modal").modal('show')
    $.ajax( 
      { 
        type: 'GET',
        url: "/question/new_comment/", 
        data:{ question_id : question_id},
        dataType: 'json', 
      })
      .done(function(response){
        $('.ask_comment_spinner').hide();
        $(".question_commentlist_modal").html(response);
      });

  }
  else{
   // # grab new comment
  var comment = $('.ask_comment_text').val();
  if (comment && question_id){
    $.ajax( 
      { 
        type: 'POST',
        url: "/question/new_comment/", 
        data:{ csrfmiddlewaretoken: $(".csrf_value").val(),question_id : question_id,comment:comment},
        dataType: 'json', 
      })
      .done(function(response){
        $('.ask_comment_text').val("");
        $(".question_commentlist_modal").html(response.html);
        $('.question_comment_count'+question_id).html(response.count)
      });
  }
  }
}


//ANSWER COMMENT GET AND POST FUNCTION 
function Answer_new_comment(answer_id,method){
  //changing title of modal according to answer or question comment type
 $('ask_comment_title').html('answer comment')
  //changing question id for new comment submision
  $('.question_comment_form').attr('data-catid',answer_id)
  $('.question_comment_form').attr('answer_or_question','answer')
   //checking type of method
  if (method == "GET"){
    $('.ask_comment_spinner').show();
    $('.question_commentlist_modal').html('')
    $("#question_comment_modal").modal('show')
    $.ajax( 
      { 
        type: 'GET',
        url: "/answer/new_comment/", 
        data:{ answer_id : answer_id},
        dataType: 'json', 
      })
      .done(function(response){
        $('.ask_comment_spinner').hide();
        $(".question_commentlist_modal").html(response);
      });

  }
  else{
   // # grab new comment
  var comment = $('.ask_comment_text').val();
  if (comment && answer_id){
    $.ajax( 
      { 
        type: 'POST',
        url: "/answer/new_comment/", 
        data:{ csrfmiddlewaretoken: $(".csrf_value").val(),answer_id : answer_id,comment:comment},
        dataType: 'json', 
      })
      .done(function(response){
        $('.ask_comment_text').val("");
        $(".question_commentlist_modal").html(response.html);
        $('.answer_comment_count'+answer_id).html(response.count)
      });
  }
  }
}

//#answer vote functio
function  Answer_Vote(answer_id,vote_type){
  if(answer_id && vote_type){
    $.ajax( 
      { 
          type:"POST", 
          url: "/answer/upvote/", 
          data:{  csrfmiddlewaretoken: $(".csrf_value").val(),
          answer_id: answer_id ,vote_type:vote_type
               },
          dataType: 'json', 
        })
        .done(function(response){
          if (vote_type == "upvote"){
            if(response.is_user_voted){
              $('.answer_upvote_class'+answer_id).attr("src","/static/img/profile/upvoted.png")
              $('.answer_downvote_class'+answer_id).attr("src","/static/img/profile/downvote.png")
              }
              else{
                $('.answer_upvote_class'+answer_id).attr("src","/static/img/profile/upvote.png")
              }
          }
          else{
            if(response.is_user_voted){
              $('.answer_downvote_class'+answer_id).attr('src','/static/img/profile/downvoted.png')
              $('.answer_upvote_class'+answer_id).attr('src','/static/img/profile/upvote.png')
              }
              else{
                $('.answer_downvote_class'+answer_id).attr('src','/static/img/profile/downvote.png')
              }
          }
          $('.answer_upvote_count'+answer_id).html(response.upvote_count)
          $('.answer_downvote_count'+answer_id).html(response.downvote_count)
        });
  }
}