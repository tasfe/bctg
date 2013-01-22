function getCat(catid,selectObj){
    $.ajax({
        url:'/cat',
        type:'get',
        data: 'catid='+catid,
        dataType:'json',
        success: function(data){
            $.each(data, function (cat_name, cat_id) {
                selectObj.add(new Option(cat_id, cat_name));
            });

        }
    });
}

$(document).ready(function() {
    $("select#cat1").change(function () {
        var str = "";
        $("select#cat1 option:selected").each(function () {
            str += $(this).val() + "";
        });
        var selectObj=document.getElementById("cat2");
        selectObj.length=0;
        selectObj.add(new Option("请选择二级类目", "-1"));
        if(str != "-1"){
            getCat($(this).val(),selectObj);
        }
        var selectObj=document.getElementById("cat3");
        selectObj.length=0;
        selectObj.add(new Option("请选择三级类目", "-1"));
    })
        .change();
});

$(document).ready(function() {
    $("select#cat2").change(function () {
        var str = "";
        $("select#cat2 option:selected").each(function () {
            str += $(this).val() + "";
        });
        var selectObj=document.getElementById("cat3");
        selectObj.length=0;
        selectObj.add(new Option("请选择三级类目", "-1"));
        if(str != "-1"){
            getCat($(this).val(),selectObj);
        }
    })
        .change();
});

$(document).ready(function() {
    $("select#cat3").change(function () {
        var str = "";
        $("select#cat3 option:selected").each(function () {
            str += $(this).val() + "";
        });
        $("li#buyernum").text("");
        $("div.buyers").display=none;
        if(str != "-1"){
            $.ajax({
                url:'/getbuyersnum',
                type:'get',
                data: 'cat3='+str,
                dataType:'json',
                success: function(data){
                    $("li#buyernum").text(data);
                }
            });
        }
    })
        .change();
});