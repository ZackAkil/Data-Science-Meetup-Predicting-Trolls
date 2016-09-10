// chrome.extension.sendMessage({}, function(response) {

	function huntTrolls(){

		var comments = $('.comment-renderer-text-content');
      	comments.each(function() {
      		$(this)
	  		.closest(".comment-renderer")
	  		.parent()
	  		.css("background-color", "beige");
      		console.log($(this).text());
      		commentScore = rateComment($(this).text().toLowerCase());
      		if (commentScore > 0){
      			actionOnTrollComment(this,commentScore);
				}
		});     
	}

	function actionOnTrollComment(trollComment,score){

		console.log($( trollComment ).text()  +' score: '+ score);
  		$(trollComment)
	  		.closest(".comment-renderer")
	  		.parent()
	  		.css("background-color", "yellow");
  		// $(".comment-renderer").hide();
	}

	function rateComment(comment){
		var score = 0;
		for (var word in wordScores) {
		    if (wordScores.hasOwnProperty(word)) {
		        if (comment.indexOf(word) !== -1)
		        	score += wordScores[word]
		    }
		}
		return score
	}

	 function pollVisibility() {
      if (!$(".action-panel-loading").is(":visible")) {
          // call a function here, or do whatever now that the div is not visible
		  huntTrolls();
		  pollInvisibility();
      } else {
          setTimeout(pollVisibility, 500);
      }
  	}

  	function pollInvisibility() {
      if ($(".action-panel-loading").is(":visible")) {
          // call a function here, or do whatever now that the div is not visible
		  pollVisibility();
      } else {
          setTimeout(pollInvisibility, 500);
      }
  	}



	var readyStateCheckInterval = setInterval(function() {
	if (document.readyState === "complete") {

		console.log("Video title err: "+ $('#eow-title').text());
		clearInterval(readyStateCheckInterval);

		// ----------------------------------------------------------
		// This part of the script triggers when page is done loading
		console.log("Hello. This message was sent from scripts/inject.js");
		// ----------------------------------------------------------

		pollVisibility();
	}
	}, 10);

	// $(window).hashchange("DOMSubtreeModified", function() {
	// 	clearInterval(readyStateCheckInterval);
	// 	console.log("Hello. This message was sent from update detection");
 //    	alert("something has been changed on page, you should update href tag");
	// });


// });
