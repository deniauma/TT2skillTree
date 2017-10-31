var skills = null;
var knight = 0;
var warlord = 0;
var sorcerer = 0;
var rogue = 0;
var sp_used = 0;
var build = {};

function init_build(){
    for(s in skills){
        build[skills[s].pk] = 0;
    }
}

function get_skill(id){
    var skill = {};
    skill.id = id;
    skill.lvl = build[id];
    for(s in skills){
        if(skills[s].pk == id){
            skill.fields = skills[s].fields;
            break;
        }
    }
    return skill;
}

function get_selected_skill(){
    var id = $('.selected').attr('id');
    return get_skill(id);
}

function display_skill(){
    var s = get_selected_skill();
    $('#skill_title').html(s.fields.name);
    $('#skill_effect1').html(s.fields['bonus_effect1_lvl'+s.lvl]);
    $('#skill_effect2').html(s.fields.bonus_effect2_lvl1);
}

function upgrade_skill(){
    var s = get_selected_skill();
    var s_req = s.fields.skill_req;
    var s_req_bool = true;
    if(s_req != null){
        req = get_skill(s_req);
        if(req.lvl == 0){
            s_req_bool = false;
        }
    }
    var sp_req = s.fields.sp_req;
    var tree_lvl = $('.tab-link.current > span').html()*1;
    if(s.lvl*1 < s.fields.max_level && s_req_bool && tree_lvl >= sp_req){
        var cost = s.fields['cost_lvl'+s.lvl];
        sp_used += cost;
    
        if(s.fields.branch == "Red"){
            knight += cost;
            $('#knight_lvl').html(knight);
        }
        if(s.fields.branch == "Yellow"){
            warlord += cost;
            $('#warlord_lvl').html(warlord);
        }
        if(s.fields.branch == "Blue"){
            sorcerer += cost;
            $('#sorcerer_lvl').html(sorcerer);
        }
        if(s.fields.branch == "Green"){
            rogue += cost;
            $('#rogue_lvl').html(rogue);
        }
        build[s.id]++
        $('.selected > .skill_lvl').html(build[s.id]);
        $('#sp_used > span').html(sp_used);
    }
    
}

$(document).ready(function(){
	
	$('ul.tabs li').click(function(){
		var tab_id = $(this).attr('data-tab');

		$('ul.tabs li').removeClass('current');
		$('.tab-content').removeClass('current');

		$(this).addClass('current');
        $("#"+tab_id).addClass('current');
        $('.selected').removeClass('selected');
        $("#"+tab_id+" > .skill_slot0").addClass('selected');
        display_skill();
    })
    
    $('.skill_btn').bind('click', function(){
        console.debug($(this).parent().attr('id'));
        $('.selected').removeClass('selected');
        $(this).parent().addClass('selected');
        display_skill();
	})

    $('#skill_btn_upgrade').bind('click', function(){
        upgrade_skill();
        display_skill();
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
        init_build();
    });

})
