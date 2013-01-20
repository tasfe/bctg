function getCat(catid){
    var respd = $.ajax({
        url:'/cat',
        type:'get',
        data: 'catid='+catid,
        dataType:'json'
    });
    return respd;
}

$(document).ready(function() {
    $("select#cat1").change(function () {
        var str = "";
        $("select option:selected").each(function () {
            str += $(this).val() + " ";
        });
        var cat = getCat($(this).val());
        var obj = cat.responseText;
        alert(obj);
        var varitem = new Option("3", "3");
        var selectObj=document.getElementById("cat2");
        selectObj.length=0;
        selectObj.add(new Option("mytest", "2"));
        $("div.text").text(cat.responseText);
    })
        .change();

});

