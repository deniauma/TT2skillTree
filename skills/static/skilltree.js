var skills = null;

function get_selected_skill(){
    var id = $('.selected').attr('id');
    var skill = {};
    skill.id = id;
    skill.lvl = $('.selected > .skill_lvl').html();
    for(s in skills){
        if(skills[s].pk == id){
            skill.fields = skills[s].fields;
            break;
        }
    }
    return skill;
}

function display_skill(){
    var s = get_selected_skill();
    $('#skill_title').html(s.fields.name);
    $('#skill_effect1').html(s.fields['bonus_effect1_lvl'+s.lvl]);
    $('#skill_effect2').html(s.fields.bonus_effect2_lvl1);
}

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
        $('.selected').removeClass('selected');
        $(this).parent().addClass('selected');
        display_skill();
	})

    $('#skill_btn_upgrade').bind('click', function(){
        var lvl = $('.selected > .skill_lvl').html();
        lvl++;
        $('.selected > .skill_lvl').html(lvl++);
        display_skill();
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
        skills = s;
    });

    display_skill();

})
