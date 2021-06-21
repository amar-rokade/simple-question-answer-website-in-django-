//author profile
$(".post_author").click(function(){
    profile_id = $(this).attr("data-catid"); 
    mainpost_author_profile(profile_id);
    }) 
  

  


    //recently asked questions
  $("#recently_asked").click(function(){
    Ask();
  })

  //my asked
 $("#my_asked").click(function(){
    var user_id = $(this).attr('data-catid')
    My_asked_question(user_id);
  })

   //my answers of questions
   $("#my_answers").click(function(){
    var user_id = $(this).attr('data-catid')
    My_answers(user_id);
  })

  
 $(".go_to_qustionslist").click(function(){
          My_asked_question();
      })




  //===============COMMENT TEXT COUNT CHARACTER=======
  $(document).ready(function() {
    var maxLen = 500;
    $('.ask_comment_text').keypress(function(event) {
        var Length = $(".ask_comment_text").val().length;
        var AmountLeft = maxLen - Length;
        $('.ask_comment_text_left').html(AmountLeft)
        if (Length == maxLen) {
            if (event.which != 48) {
                return false;
            }
        }
    });
  });


 //questions vote :
 $('.question_vote').click(function(e){
  e.preventDefault();
  var question_id = $(this).attr('question_id')
  var vote_type = $(this).attr('vote-type')
  Quetion_upvote(question_id,vote_type);
})

//answer vote 
$('.answer_vote').click(function(e){
  e.preventDefault();
  var answer_id = $(this).attr('answer_id')
  var vote_type = $(this).attr('vote-type')
  Answer_Vote(answer_id,vote_type);
})


 //answer comment modal click event to show comment list
  $(".answer_comment").click(function(){
    Answer_new_comment($(this).attr('answer_id'),$(this).attr('method'))
  })

   //question comment modal click event to show comment list
   $('.question_comment').click(function(){
    Question_new_comment($(this).attr('question_id'),$(this).attr('method'))
  })


//ask  new comment form submit  either question or answer 
$('.question_comment_form').submit(function(e){
  e.preventDefault();
  var id = $(this).attr('data-catid')
  var answer_or_question = $(this).attr('answer_or_question')
  if (answer_or_question == 'question'){
    Question_new_comment(id);
  }
  else {
    Answer_new_comment(id)
  }
})