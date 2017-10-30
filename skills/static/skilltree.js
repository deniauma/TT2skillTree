$(document).ready(function(){
	
	$('ul.tabs li').click(function(){
		var tab_id = $(this).attr('data-tab');

		$('ul.tabs li').removeClass('current');
		$('.tab-content').removeClass('current');

		$(this).addClass('current');
		$("#"+tab_id).addClass('current');
    })
    
    $('.skill_btn').bind('click', function(){
        console.debug($(this).parent().attr('id'));
	})

    $('#skill_btn_upgrade').bind('click', function(){
        var lvl = $('.selected > .skill_lvl').html();
        lvl++;
        $('.selected > .skill_lvl').html(lvl++);
        console.debug(lvl);
    })

    $.ajax({
        method: "GET",
        url: "getskills/all",
    })
    .done(function( msg ) {
        //console.debug(msg["skills"]);
        data = msg["skills"];
        s = JSON.parse(data);
        console.debug("Test: "+s.length+", "+s[0].pk)
    });

})
