# coding:utf-8
import re

test_html = """<body oncontextmenu="return false"
oncopy="document.selection.empty()">
    <script type="text/javascript"
    src="http://img.jyeoo.net/scripts/jquery1.7.2min.js"></script><script
    type="text/javascript" src="http://img.jyeoo.net/scripts/jye-2017.02.08
    .min.js"></script><script type="text/javascript">var
    imageRootUrl="http://img.jyeoo.net/",wwwRootUrl="http://www.jyeoo.com/",
    blogRootUrl="http://blog.jyeoo.com/",
    spaceRootUrl="http://space.jyeoo.com/",loginUrl="http://www.jyeoo.com/",
    logoutUrl="http://www.jyeoo.com/account/logoff",
    scriptsUrl="http://img.jyeoo.net/scripts/",isMobile=false;var
    mustyleAttr={color:"#000000",fontsize:"13px",fontfamily:"arial",
    displaystyle:"true"};document.domain="jyeoo.com";jyeoo.setUser(
    '60597b42-c783-46f3-a736-023ec9c9df11','20922938','okayxueke',
    'okayxueke@163.com','True');function preventDefault(e) { try {
    e.stopPropagation(); e.preventDefault(); } catch (x) { e.cancelBubble =
    true; e.returnValue = false; } return false; }if (
    navigator.userAgent.indexOf('MSIE') < 0) { var css =
    document.createElement('style'); css.type = 'text/css'; css.innerHTML =
    'body{-moz-user-select:none;-webkit-user-select:none;}';
    document.getElementsByTagName('head')[0].appendChild(css);
    }document.oncopy = function () { return preventDefault(window.event ||
    arguments[0]); };document.onkeydown = function () { var e = window.event
    || arguments[0]; var c = e.keyCode || e.which; if (c == 16 || c == 17 ||
    c == 18) { return preventDefault(e); } };$.ajaxSetup({
    cache:true});</script><script type="text/javascript"
    src="http://img.jyeoo.net/scripts/MLCore-2013.08.15.min.js"></script
    ><script type="text/javascript"
    src="http://www.jyeoo.com/content/scripts/tinyedit/core.js?v=20140703
    "></script><script type="text/javascript"
    src="http://img.jyeoo.net/scripts/jplugins-2012.03.16.min.js"></script>




    <div id="borwserWarning" style="display:none; width:100%;  line-height:
    20px;  opacity: 0.8; position:fixed;z-index:999;">
        <div class="warp" style="text-align: center; color: #996512;
        background: #FFE2B4; border: 1px solid #BB780D; border-top: none; ">
            <span>为了更流畅的使用菁优平台，请将您浏览器的极速模式切换为兼容模式,或使用IE8及以上版本的浏览器</span>
            <a href="javascript:void(0)" style="text-decoration:underline;"
            onclick="_closeWarning()">关闭</a>
        </div>
    </div>

<style type="text/css">
    .top .tr .vip110 { vertical-align: middle; }
</style>
<div class="top">
    <div class="tl">
            <a href="http://www.jyeoo.com/" target="_blank">首页</a>
            <em class="m6">|</em>
            <div>
                <span>应用<label class="caret"></label></span>
                <ul>
                    <li><a href="/wenda" target="_blank">问答</a></li>
                    <li><a href="/training" target="_blank">训练</a></li>
                    <li><a href="/paper" target="_blank">组卷</a></li>
                </ul>
            </div>
            <em class="m6">|</em>
            <div id="header_app">
                <span>APP<label class="caret"></label></span>
                <ul>
                    <li><a href="/appstore?tp=0" target="_blank">菁优网</a></li>
                    <li><a href="/appstore?tp=1" target="_blank">i培训</a></li>
                </ul>
            </div>
            <em class="m6">|</em>
            <a href="http://i.jyeoo.com/" target="_blank">i培训</a>
            <em class="m6">|</em>
            <a href="http://xyh.jyeoo.com/" target="_blank"
            style="color:#169BEF;">校园号</a>
            <em class="m6">|</em>
    </div>
    <div class="tr">
        <a href="/recharge" target="_blank" rel="nofollow"><em>充值</em></a><em
        class="m6">|</em>
            <span>okayxueke</span>
            <em class="m6"></em>
            <a href="http://space.jyeoo.com/" target="_blank"><em>我的空间</em></a>
            <em class="m6">|</em>
            <a href="http://www.jyeoo.com/account/logoff"><em>退出</em></a>
    </div>
</div>
    <div class="clear"></div>
    <div class="warp head">

<div class="logo">
    <a href="http://www.jyeoo.com/"><img
    src="http://img.jyeoo.net/images/logo_1.png" alt="菁优网" title="菁优网"
    height="70" class="fleft"></a>
        <div style="float:right" id="ja046"></div>
</div>
<div class="search" id="searchform">
    <form action="/search" method="get" target="_blank">
        <input type="hidden" value="0" id="c" name="c">
        <div class="search-form">
            <div class="search-ques">
                <em>试&nbsp;题</em>&nbsp;<span class="caret"></span>
                <ul class="dropdown-menu">
                    <li><a href="javascript:void(0)" onclick="_setc(this)"
                    data-sq="0" data-ph="">试&nbsp;题</a></li>
                    <li><a href="javascript:void(0)" onclick="_setc(this)"
                    data-sq="1" data-ph="">试&nbsp;卷</a></li>
                </ul>
            </div>
            <input class="search-text" type="text" maxlength="90" id="qb"
            name="qb" placeholder="">
            <img class="search-img"
            src="http://img.jyeoo.net/images/eqsearch2.jpg" id="mathmlHelper"
            alt="输入公式" title="输入公式">
            <input class="search-submit" type="submit" value="搜索">
        </div>
    </form>
</div>
<a href="http://www.jyeoo.com/wenda" style="float: left; line-height: 90px;
font-size: 14px; text-decoration: underline;" target="_blank"
title="在线问答">我要提问</a>
<div class="clear"></div>
    </div>
    <div class="clear"></div>

<style type="text/css">
    .lbs { position: relative; display: inline-block; }
    .lbs > label { font-size: 13px; line-height: 40px; display: inline-block;
    color: white; float: left; padding: 0 15px; }
    .lbs .province { position: absolute; left: 0; top: 40px; width: 220px;
    background: #aee3ff; border: 1px solid #7ecdff; font-size: 12px;
    text-align: left; display: none; }
    .lbs .city { position: absolute; left: 220px; top: 40px; width: 220px;
    background: #aee3ff; border: 1px solid #7ecdff; font-size: 12px;
    text-align: left; display: none; }
    .lbs .province a, .lbs .city a { color: #09757c; padding: 3px 8px;
    display: inline-block; white-space: nowrap; text-decoration: underline;
    line-height: normal; float: left; min-width: 3em; }
    .lbs .province a.cur { color: white; font-weight: bold; }
</style>
<div class="nav">
    <div class="warp" style="position:relative">
        <ul>
            <li style="position:relative;">
                <span class="btn-ui menus">初中化学<span
                class="caret"></span></span>
                <ul class="center">
                    <li>
                        <span class="group-root">小学</span>
                        <div class="root-chd">
                                <a href="/math3/ques/search">数学</a>
                        </div>
                    </li>
                    <li>
                        <span class="group-root">初中</span>
                        <div class="root-chd">
                                <a href="/math/ques/search">数学</a>
                                <a href="/physics/ques/search">物理</a>
                                <a href="/chemistry/ques/search">化学</a>
                                <a href="/bio/ques/search">生物</a>
                                <a href="/geography/ques/search">地理</a>
                                <a href="/chinese/ques/search">语文</a>
                                <a href="/english/ques/search">英语</a>
                                <a href="/politics/ques/search">政治</a>
                                <a href="/history/ques/search">历史</a>
                        </div>
                    </li>
                    <li>
                        <span class="group-root">高中</span>
                        <div class="root-chd">
                                <a href="/math2/ques/search">数学</a>
                                <a href="/physics2/ques/search">物理</a>
                                <a href="/chemistry2/ques/search">化学</a>
                                <a href="/bio2/ques/search">生物</a>
                                <a href="/geography2/ques/search">地理</a>
                                <a href="/chinese2/ques/search">语文</a>
                                <a href="/english2/ques/search">英语</a>
                                <a href="/politics2/ques/search">政治</a>
                                <a href="/history2/ques/search">历史</a>
                        </div>
                    </li>
                </ul>
            </li>
        </ul>
        <ul style="float:right;">
            <li style="width:120px;position:relative;">
                <span>我的组卷<span class="caret"></span></span>
                <ul class="center" style="width:118px;">
                    <li><a href="http://space.jyeoo.com/favorite?sb=22&amp;tp
                    =2" target="_blank">历史组卷</a></li>
                    <li><a href="http://space.jyeoo.com/favorite?sb=22&amp;tp
                    =3" target="_blank">我的下载</a></li>
                    <li><a href="http://space.jyeoo.com/favorite?sb=22&amp;tp
                    =0" target="_blank">试题收藏</a></li>
                    <li><a href="http://space.jyeoo.com/favorite?sb=22&amp;tp
                    =1" target="_blank">试卷收藏</a></li>
                </ul>
            </li>
        </ul>
        <div class="ques-cart">
            <div class="info">
                <span>选择题<em id="xzCount">0</em></span>
                <span>填空题<em id="tkCount">0</em></span>
                <span>解答题<em id="jdCount">0</em></span>
                <span><a href="javascript:void(0)" class="btn-ui del1"
                onclick="QuesCart.clear('chemistry',null,null)">清空</a> </span>
                <span><a href="javascript:void(0)" class="edit"
                onclick="QuesCart.load('chemistry',
                '初中化学在线组卷')">进入组卷中心</a></span>
            </div>
            <div class="title "><span class="btn-ui cart"
            style="line-height:20px;display:inline-block;*margin-top:12px
            ">试题篮</span> </div>
        </div>
    </div>
</div>
<script type="text/javascript">
    $.fn.initLBS = function (level, callback) {
        $(this).each(function (index, element) {
            var self = $(this).append("<label>地区</label><span class=\"caret\"
            style=\"*margin-top: 20px;margin-left: -12px;\"></span>"),
            no = self.data("no"), label = self.children("label");
            var province = $("<div class=\"province\"></div>").appendTo(self);
            var city = $("<div class=\"city\"><a href=\"javascript:void(0)\"
            data-no=\"\">全省</a></div>").appendTo(self);
            self.hover(function () { province.show(); no = self.data("no");
            $("a.cur", province).removeClass("cur") }, function () {
            province.hide(); city.hide(); });

            $.post("/api/area1", {}, function (data) {
                if (data.S == 1) {
                    return true;
                }
                $("<a href=\"javascript:void(0)\"
                data-no=\"\">全部</a>").appendTo(province);
                for (var i = 0; i < data.D.length; i++) {
                    $("<a  href=\"javascript:void(0)\" data-no=" + data.D[
                    i].ID + "  data-type=" + data.D[i].Type + ">" + data.D[
                    i].Name + "</a>").appendTo(province);
                    if (no == data.D[i].ID) {
                        label.html(data.D[i].Name);
                    }
                }

                $.post("/api/area2", { code: no }, function (data) {
                    if (data.S == 1) {
                        return true;
                    }
                    for (var i = 0; i < data.D.length; i++) {
                        if (no == data.D[i].ID) {
                            label.html(data.D[i].Name);
                        }
                    }
                });

                province.find("a").each(function () {
                    var p = $(this);
                    p.click(function () {
                        $("a.cur", province).removeClass("cur"); p.addClass(
                        "cur");
                        if ($(this).data("type") == "-1") {
                            cLBS($(this));
                        }
                        else {
                            pLBS(p);
                        }
                    });
                });
            });

            function pLBS(el) {
                var el = $(el), pno = el.data("no");
                if (level == "1" || pno == "") {
                    cLBS(el);
                }
                else {
                    $.post("/api/area2", { code: pno }, function (data) {
                        if (data.S == 1) {
                            return true;
                        }
                        city.empty().show();
                        $("<a href=\"javascript:void(0)\" data-no=" + pno +
                        ">全省</a>").appendTo(city);
                        for (var i = 0; i < data.D.length; i++) {
                            $("<a  href=\"javascript:void(0)\" data-no=" +
                            data.D[i].ID + ">" + data.D[i].Name +
                            "</a>").appendTo(city);
                            if (no == data.D[i].ID) {
                                label.html(data.D[i].Name);
                            }
                        }
                        city.find("a").each(function () {
                            var c = $(this);
                            c.click(function () {
                                if (pno == c.data("no")) {
                                    cLBS(el);
                                }
                                else {
                                    cLBS(c);
                                }
                            });
                        });
                    });
                }
            }

            function cLBS(el) {
                var el = $(el), cno = el.data("no");
                callLBS(cno, el.html());
            }

            function callLBS(code, text) {
                self.data("no", code);
                label.html(code == '' ? "地区" : text);
                province.hide();
                city.empty().hide();
                if ($.isFunction(callback) && code != no) {
                    callback(code, text);
                }
            }
        });
    }

    $(function () {
        $(".lbs").data("no", $.cookie('j_q_lbs')).initLBS('2', function (
        code, text) { setLBS(code, text); });
    });
</script>        <div class="clear"></div>
    <div style="width:100%; background:">
        <div class="warp content" id="cont">


<div class="clear"></div>
<div class="ques-detail">
    <div class="c10"></div>
    <div id="ja009"><a
    href="http://a.jyeoo.com/go?id=b5c7f38096e24257a4d2b39931d7a093&amp;u
    =73E2B681690B4D884FE0F056CD64558C8B8DC1965A463E6E30520B65FE0CC81F"
    target="_blank" title="高考试题分类汇编"><img
    src="http://img.jyeoo.net/ad/f19a76628d654609a4592bbe29c588a4.png"
    style="display: none !important;"></a></div>
    <div class="c5"></div>
    <div style="overflow:hidden">
        <div style="float:right;width:260px;overflow:hidden"
        class="detail-right">
            <div id="ja031"><a
            href="http://a.jyeoo.com/go?id=0d27aa496476417a85621d14881c6927
            &amp;u=348F48E5A3787153964D91C0B8F89324455C9F632B081F13C6BDB7C6BA15333C" target="_blank" title="VIP"><img src="http://img.jyeoo.net/ad/1365151d135f4af1a18d2726bf1b8d14.gif" style="display: none !important;"></a></div>
            <div class="c5"></div>
            <div id="ja033"><a
            href="http://a.jyeoo.com/go?id=19376df514d64a56954573e23f110393
            &amp;u=348F48E5A3787153964D91C0B8F893247FFFCDA7465F00EF82DB0B85E6D527D4" target="_blank" title="APP"><img src="http://img.jyeoo.net/ad/b83eb3fa55a448c8b9e9209e29c1308e.png" style="display: none !important;"></a></div>
            <div class="ques-reports">
                <div class="qtitle"><h1>推荐试卷</h1></div>
            <ul><li><em>·</em><a
            href="http://www.jyeoo.com/chemistry/report/detail/74971c34-fdea
            -4d87-a676-0de4b32070c1" target="_blank"
            title="2012年甘肃省定西市中考化学模拟试卷（二）">2012年甘肃省定西市中考化学模拟试卷（二）</a></li><li
            ><em>·</em><a href="http://www.jyeoo.com/chemistry/report/detail
            /bcee0aae-d28f-4582-891c-4f8abb65575c" target="_blank"
            title="2013年甘肃省定西市渭源县北寨中学中考化学模拟试卷">2013年甘肃省定西市渭源县北寨中学中考化学模拟试卷</a
            ></li><li><em>·</em><a
            href="http://www.jyeoo.com/chemistry/report/detail/9a9a6c1e-66a5
            -4308-9db4-20421d68ad51" target="_blank"
            title="2017年广东省梅州市丰顺县东海中学中考化学模拟试卷（十二）">2017
            年广东省梅州市丰顺县东海中学中考化学模拟试卷（十二）</a></li></ul></div>
            <div class="c5"></div>
            <div class="ques-videos" style="display: block;">
                <div class="qtitle"><h1>知识点视频</h1></div>
                <div id="ja011"><div class="point-video"><a
                href="http://a.jyeoo.com/go?id
                =2f85c76cf68b42e4aaf5bc27ed70a2fe&amp;u
                =348F48E5A3787153964D91C0B8F8932427E6952E95F7EADFECCE0318DA2F237B38D8A7DD126E1A07A158AE928F4C207CAE11842C51194863AE23E3CAC9DBFF2ACFB87C020D2BFA1544FCB2D0C848F64C3F1CA718915A46A1" target="_blank"><em class="btn-ui video"></em>质量守恒定律的宏观解释-反应前后可能改变</a></div></div>
            </div>
            <div class="c5"></div>
            <div class="ques-xyh" style="display: block;">
                <div class="qtitle"><h1>校园号</h1>本地优质教育机构</div>
                <div id="ja035"><ul><li><a
                href="http://a.jyeoo.com/go?id
                =d1ad7e53e92647d2b8c2329f78b01db7&amp;u
                =E817F7F5D086223B6BA3C1BCD809332788753A119A00E7636FA41C1174501AE4685D2447FCAF9842F33C6D303AE606845CBFF25146DC7BA3259E43878CCBE7459ADD31086AE108C3FDBC0C65E7C5F006" target="_blank">新思维博智教育咨询有限公司</a></li><li><a href="http://a.jyeoo.com/go?id=bc3446d719c44ef4b3454f8fbaf5b29d&amp;u=E817F7F5D086223B6BA3C1BCD809332788753A119A00E7636FA41C1174501AE418737B1C734FE314EC41F159820CE0102F300552C1363AFB0479BC43170EBEE9CFB482453160946DE406E71BC4CF51D2" target="_blank">人人学教育</a></li><li><a href="http://a.jyeoo.com/go?id=7573dd084be24d5786b7009dfaeb4f12&amp;u=E817F7F5D086223B6BA3C1BCD809332788753A119A00E7636FA41C1174501AE4A6ADB9EFDC5A69814C12B7522281209E466F6EA845D8FA75BA83A644BC380185C7B4D59AB2BDD757BCF7CE9DE4E567C5" target="_blank">北京市十一学校</a></li><li><a href="http://a.jyeoo.com/go?id=0b3f366b996342f69236acba7714d8f7&amp;u=E817F7F5D086223B6BA3C1BCD809332788753A119A00E7636FA41C1174501AE43DF6762E59DABA587C15B3E066BF5451ED0F6FF52984FFC471F68AD380F6A5804D2E9616005ACF634DED97B2CCA41957" target="_blank">北京市海淀区学而思培训学校</a></li></ul><a href="http://xyh.jyeoo.com/home/join#3" target="_blank" class="fright" onclick="return openCampusForm(this)">+我也要加入</a></div>
            </div>
        </div>
        <div style="float:left;width:720px;overflow:hidden">
            <div style="background:white;"><fieldset
            id="5518724c-6cc8-4b8d-9d0c-a4c97f4d2440" class="quesborder"
            s="chemistry"><div class="pt1"><!--B1--><span
            class="qseq"></span><a
            href="http://www.jyeoo.com/chemistry/report/detail/9a9a6c1e-66a5
            -4308-9db4-20421d68ad51"
            target="_blank">（2017•丰顺县校级模拟）</a>已知化学方程式X+2O<sub>2</sub><span
            dealflag="1" class="MathJye" mathtag="math"
            style="whiteSpace:nowrap;wordSpacing:normal;wordWrap:normal
            "><table cellpadding="-1" cellspacing="-1"
            style="margin-right:1px"><tbody><tr><td style="border-bottom:1px
            solid black;padding-bottom:1px;font-size:90%"><table
            style="margin-right:1px" cellspacing="-1"
            cellpadding="-1"><tbody><tr><td>&nbsp;点燃&nbsp;</td></tr><tr><td
            style="font-size:90%"><div style="border-top:1px solid
            black;line-height:1px">.</div></td></tr></tbody></table></td></tr
            ><tr><td>&nbsp;</td></tr></tbody></table></span>CO<sub>2</sub>+2H
            <sub>2</sub>O，下列对X的判断不正确的是（　　）<!--E1--></div><div
            class="pt2"><!--B2--><table style="width:100%" class="ques
            quesborder"><tbody><tr><td style="width:98%"
            class="selectoption"><label class="
            s">A．X一定含碳、氢、氧三种元素</label></td></tr><tr><td style="width:98%"
            class="selectoption"><label
            class="">B．X是一种最简单的有机物</label></td></tr><tr><td style="width:98%"
            class="selectoption"><label
            class="">C．X是一种重要的气体燃料</label></td></tr><tr><td style="width:98%"
            class="selectoption"><label
            class="">D．X的化学式是CH<sub>4</sub></label></td></tr></tbody></table
            ><!--E2--></div><div class="ptline"></div><div
            class="pt3"><!--B3--><em>【考点】</em><a
            href="http://www.jyeoo.com/chemistry/ques/detail/5518724c-6cc8
            -4b8d-9d0c-a4c97f4d2440" onclick="openPointCard('chemistry',
            'G1');return false;">质量守恒定律及其应用</a>．<!--E3--></div><div
            class="pt4"><!--B4--><em>【专题】</em>化学用语和质量守恒定律．<!--E4--></div><div
            class="pt5"><!--B5--><em>【分析】</em>由题目中：化学方程式X+2O<sub>2</sub>
            <span dealflag="1" class="MathJye" mathtag="math"
            style="whiteSpace:nowrap;wordSpacing:normal;wordWrap:normal
            "><table cellpadding="-1" cellspacing="-1"
            style="margin-right:1px"><tbody><tr><td style="border-bottom:1px
            solid black;padding-bottom:1px;font-size:90%"><table
            style="margin-right:1px" cellspacing="-1"
            cellpadding="-1"><tbody><tr><td>&nbsp;点燃&nbsp;</td></tr><tr><td
            style="font-size:90%"><div style="border-top:1px solid
            black;line-height:1px">.</div></td></tr></tbody></table></td></tr
            ><tr><td>&nbsp;</td></tr></tbody></table></span>CO<sub>2</sub>+2H
            <sub>2</sub>O，则可知：X的物质分类（有机物）；X的元素组成；X是否为燃料；X的化学式．<!--E5--></div
            ><div class="pt6"><!--B6--><em>【解答】</em>解：已知化学方程式X+2O<sub>2</sub>
            <span dealflag="1" class="MathJye" mathtag="math"
            style="whiteSpace:nowrap;wordSpacing:normal;wordWrap:normal
            "><table cellpadding="-1" cellspacing="-1"
            style="margin-right:1px"><tbody><tr><td style="border-bottom:1px
            solid black;padding-bottom:1px;font-size:90%"><table
            style="margin-right:1px" cellspacing="-1"
            cellpadding="-1"><tbody><tr><td>&nbsp;点燃&nbsp;</td></tr><tr><td
            style="font-size:90%"><div style="border-top:1px solid
            black;line-height:1px">.</div></td></tr></tbody></table></td></tr
            ><tr><td>&nbsp;</td></tr></tbody></table></span>CO<sub>2</sub>+2H
            <sub>2</sub>O，则可知：<br>A、根据质量守恒定律的元素守恒可知，X只含有碳元素、氢元素，而无氧元素，故A
            判断错误；<br>B、根据质量守恒定律的元素守恒可知，X中含有碳元素，其可燃烧，具有有机物的特点，推测其化学式为CH<sub>4
            </sub>，则为一种最简单的有机化合物，故B判断正确；<br>C、由化学方程式可知，X可以燃烧，所以是一种重要的气体燃料，故C
            判断正确；<br>D、根据质量守恒定律的元素守恒可知，可推测其化学式为CH<sub>4</sub>，故D判断正确．<br>故选A
            ．<!--E6--></div><div
            class="pt7"><!--B7--><em>【点评】</em
            >本题是运用化学中的基本思想质量守恒思想；学会分析此类题目：仔细查清反应前后的元素种类，原子个数．<!--E7--></div
            ><div class="pt9"><span
            class="qcp">声明：本试题解析著作权属菁优网所有，未经书面同意，不得复制发布。</span><!--B9--><span
            >答题：<input type="button" class="vip210"
            disabled="">起点线老师　2012/12/29</span><!--E9--></div></fieldset
            ><span class="fieldtip"><label
            style="float:right;margin-right:10px" title="“难度系数(
            系数值区间为0~1)”反映试题的难易程度。
系数值越大，试题就越容易；系数值越小，试题难度越大">难度：<em style="color:red">0.66</em></label><label
style="float:right;margin-right:10px" title="“真题次数”指试题在大型考试中出现的次数。
次数越多，试题常考指数越高；次数越少，试题常考指数越低。">真题：<em style="color:red">3</em></label><label
style="float:right;margin-right:10px" title="“组卷次数”指试题在用户组卷过程中被使用的次数。
次数越多，试题热度越高；次数越少，试题热度越低。">组卷：<em style="color:red">109</em></label><a
href="http://www.jyeoo.com/chemistry/ques/detail/5518724c-6cc8-4b8d-9d0c
-a4c97f4d2440" onclick="closeBox();Test2.testDoing(this,'chemistry',
'5518724c-6cc8-4b8d-9d0c-a4c97f4d2440',3);return false"><em class="btn-ui
test"></em>训练</a><a href="http://www.jyeoo.com/chemistry/ques/detail/5518724c
-6cc8-4b8d-9d0c-a4c97f4d2440" onclick="closeBox();Test2.favorite(this,
'chemistry','5518724c-6cc8-4b8d-9d0c-a4c97f4d2440',0);return false"><em
class="btn-ui favo"></em>收藏</a><a href="javascript:void(0)"
onclick="openConfirm('【下载确认】','chemistry',
'5518724c-6cc8-4b8d-9d0c-a4c97f4d2440','1')"><em class="btn-ui
down"></em>下载</a><a title="点击将把本题加入或移出您的试题篮" class="btn-ui
add">试题篮</a></span></div>
            <div class="c20"></div>
            <div class="ques-related">
                <div class="qtitle">
                    <h1>进阶学习</h1>
                    <em style="padding:0 15px"></em>
                    <a href="javascript:void(0)" class="cur">中考题</a>
                    <a href="javascript:void(0)">常考题</a>
                    <a href="javascript:void(0)">好题</a>
                    <a href="javascript:void(0)">易错题</a>
                    <a href="javascript:void(0)">热搜题</a>
                    <a href="javascript:void(0)">难题</a>
                </div>
            <ul style="display: block;"><li><a
            href="http://www.jyeoo.com/chemistry/ques/detail/cfdfe80e-7a25
            -4f88-b62d-a7a53b8a982b" target="_blank"><span
            class="qseq"></span>（2016
            •兰州）把一定质量的甲、乙、丙、丁四种物质放入一密闭容器中，在一定条件下反应一段时间，测得反应后各物质的质量如下，则下列说法中错误的是（　　）<table class="edittable"><tbody><tr><td width="114">物质</td><td width="114">甲</td><td width="114">乙</td><td width="114">丙</td><td width="114">丁</td></tr><tr><td>反应前的质量（g）</td><td>7.6</td><td>2.0</td><td>0.2</td><td>0</td></tr><tr><td>反应后的质量（g）</td><td>3.2</td><td>X</td><td>5.8</td><td>0.4</td></tr></tbody></table></a></li><li><a href="http://www.jyeoo.com/chemistry/ques/detail/4007a8d4-dcb7-4ba9-ae1d-749af757c007" target="_blank"><span class="qseq"></span>（2016•娄底模拟）化学反应前后，下列各项中，肯定没有变化的是（　　）①原子数目&nbsp;&nbsp;②原子的种类&nbsp;&nbsp;③分子数目&nbsp;&nbsp;④分子的种类&nbsp;&nbsp;&nbsp;⑤元素的种类&nbsp;&nbsp;⑥物质的总质量&nbsp;&nbsp;⑦物质的种类．</a></li><li><a href="http://www.jyeoo.com/chemistry/ques/detail/935c8b36-75bd-45f3-81fd-17cdc647a8a8" target="_blank"><span class="qseq"></span>（2016•百色）煤油中含有噻吩，噻吩（用X表示）有令人不愉快的气味，其燃烧的化学方程式可表示为：X+6O<sub>2</sub><span dealflag="1" class="MathJye" mathtag="math" style="whiteSpace:nowrap;wordSpacing:normal;wordWrap:normal"><table cellpadding="-1" cellspacing="-1" style="margin-right:1px"><tbody><tr><td style="border-bottom:1px solid black;padding-bottom:1px;font-size:90%"><table style="margin-right:1px" cellspacing="-1" cellpadding="-1"><tbody><tr><td>&nbsp;点燃&nbsp;</td></tr><tr><td style="font-size:90%"><div style="border-top:1px solid black;line-height:1px">.</div></td></tr></tbody></table></td></tr><tr><td>&nbsp;</td></tr></tbody></table></span>4CO<sub>2</sub>+SO<sub>2</sub>+2H<sub>2</sub>O，则噻吩X的化学式为（　　）</a></li><li><a href="http://www.jyeoo.com/chemistry/ques/detail/44c2fd80-e73f-4935-8c8c-cec8eaa84741" target="_blank"><span class="qseq"></span>（2016•齐齐哈尔）在催化剂并加热的条件下，氨气和氧气能发生化学反应，其反应的化学方程式为4NH<sub>3</sub>+5O<sub>2</sub><span dealflag="1" class="MathJye" mathtag="math" style="whiteSpace:nowrap;wordSpacing:normal;wordWrap:normal"><table cellpadding="-1" cellspacing="-1" style="margin-right:1px"><tbody><tr><td style="border-bottom:1px solid black;padding-bottom:1px;font-size:90%"><table style="margin-right:1px" cellspacing="-1" cellpadding="-1"><tbody><tr><td>&nbsp;催化剂&nbsp;</td></tr><tr><td style="font-size:90%"><div style="border-top:1px solid black;line-height:1px">.</div></td></tr></tbody></table></td></tr><tr><td>△</td></tr></tbody></table></span>4X+6H<sub>2</sub>O，则X的化学式是（　　）</a></li><li><a href="http://www.jyeoo.com/chemistry/ques/detail/7a2330fa-434c-47d1-b1ad-4bf81934234b" target="_blank"><span class="qseq"></span>（2016•随州）在一定条件下，甲、乙、丙、丁四种物质在一密闭容器中充分反应，测得反应前后个物质的质量如表所示．根据表中信息判断下列说法正确的是（　　）<table class="edittable"><tbody><tr><td width="186">物质</td><td width="62">甲</td><td width="59">乙</td><td width="59">丙</td><td width="59">丁</td></tr><tr><td>反应前的质量/g</td><td>2</td><td>30</td><td>20</td><td>10</td></tr><tr><td>反应后的质量/g</td><td>m</td><td>39</td><td>5</td><td>16</td></tr></tbody></table></a></li></ul><ul style="display: none;"><li><a href="http://www.jyeoo.com/chemistry/ques/detail/b0bbd71d-cdda-440f-baae-37008c8727c4" target="_blank"><span class="qseq"></span>（2017•丰顺县校级模拟）蜡烛在空气中燃烧时，共烧掉Ag蜡烛，用去Bg氧气，生成Cg水和Dg二氧化碳，反应物的总质量为W<sub>1</sub>g，生成物的总质量为W<sub>2</sub>g，则下列选项中错误的是（　　）</a></li><li><a href="http://www.jyeoo.com/chemistry/ques/detail/c4d5cded-09db-400d-8666-045b435a8507" target="_blank"><span class="qseq"></span>（2017•丰顺县校级模拟）在化学反应A+2B═C+D中，5.6gA和7.3gB恰好完全反应，生成12.7gC，同时得到D的质量是（　　）</a></li><li><a href="http://www.jyeoo.com/chemistry/ques/detail/44c2fd80-e73f-4935-8c8c-cec8eaa84741" target="_blank"><span class="qseq"></span>（2016•齐齐哈尔）在催化剂并加热的条件下，氨气和氧气能发生化学反应，其反应的化学方程式为4NH<sub>3</sub>+5O<sub>2</sub><span dealflag="1" class="MathJye" mathtag="math" style="whiteSpace:nowrap;wordSpacing:normal;wordWrap:normal"><table cellpadding="-1" cellspacing="-1" style="margin-right:1px"><tbody><tr><td style="border-bottom:1px solid black;padding-bottom:1px;font-size:90%"><table style="margin-right:1px" cellspacing="-1" cellpadding="-1"><tbody><tr><td>&nbsp;催化剂&nbsp;</td></tr><tr><td style="font-size:90%"><div style="border-top:1px solid black;line-height:1px">.</div></td></tr></tbody></table></td></tr><tr><td>△</td></tr></tbody></table></span>4X+6H<sub>2</sub>O，则X的化学式是（　　）</a></li><li><a href="http://www.jyeoo.com/chemistry/ques/detail/d340c4ac-6e30-4294-962d-36e63426894e" target="_blank"><span class="qseq"></span>（2016•肥城市模拟）下列对课本中的原理、图表、数据的使用，叙述不正确的是（　　）</a></li><li><a href="http://www.jyeoo.com/chemistry/ques/detail/be0cc677-2ec8-4fab-a014-be7259b7315e" target="_blank"><span class="qseq"></span>（2017•罗平县一模）在化学反应前后，下列各项肯定没有变化的是（　　）①原子的种类&nbsp;&nbsp;&nbsp;②物质的总质量&nbsp;&nbsp;③元素的种类&nbsp;&nbsp;&nbsp;④分子的数目&nbsp;&nbsp;&nbsp;⑤物质的种类&nbsp;&nbsp;&nbsp;⑥原子的数目．</a></li></ul><ul style="display: none;"><li><a href="http://www.jyeoo.com/chemistry/ques/detail/fe5eef98-135a-48fe-bf60-ea9324a27015" target="_blank"><span class="qseq"></span>（2017•罗平县一模）一个密闭容器中加入甲、乙、丙、丁四种物质，在一定条件下发生化学反应，测得数据见表．下列说法中不正确的是（　　）<table class="edittable"><tbody><tr><td width="195">物质</td><td width="85">甲</td><td width="83">乙</td><td width="84">丙</td><td width="85">丁</td></tr><tr><td>反应前质量</td><td>8g</td><td>35g</td><td>5g</td><td>8g</td></tr><tr><td>反应后质量</td><td>2g</td><td>X</td><td>5g</td><td>42g</td></tr></tbody></table></a></li><li><a href="http://www.jyeoo.com/chemistry/ques/detail/be0cc677-2ec8-4fab-a014-be7259b7315e" target="_blank"><span class="qseq"></span>（2017•罗平县一模）在化学反应前后，下列各项肯定没有变化的是（　　）①原子的种类&nbsp;&nbsp;&nbsp;②物质的总质量&nbsp;&nbsp;③元素的种类&nbsp;&nbsp;&nbsp;④分子的数目&nbsp;&nbsp;&nbsp;⑤物质的种类&nbsp;&nbsp;&nbsp;⑥原子的数目．</a></li><li><a href="http://www.jyeoo.com/chemistry/ques/detail/b9ab154e-6ad3-4fee-bbbb-20f41a0bcd9a" target="_blank"><span class="qseq"></span>（2016秋•长沙县期中）化学反应前后，下列各项一定会发生变化的是（　　）</a></li><li><a href="http://www.jyeoo.com/chemistry/ques/detail/0e7171e3-9dce-4f3f-b7a6-de8b990d50a1" target="_blank"><span class="qseq"></span>（2016•湖北）AgNO<sub>3</sub>固体见光或受热易分解，故保存在棕色瓶中，AgNO<sub>3</sub>见光分解时产生一种有刺激性气味的气体，该气体可能是（　　）</a></li><li><a href="http://www.jyeoo.com/chemistry/ques/detail/558eadb0-a151-4415-8977-c7d39a34bdf7" target="_blank"><span class="qseq"></span>（2016•怀化）将一定质量的a，b，c，d四种物质放入一密闭容器中，在一定条件下反应一段时间后，测得各物质的质量如表：<table class="edittable"><tbody><tr><td width="114"><b>物质</b></td><td width="54"><b>a</b></td><td width="57"><b>b</b></td><td width="47"><b>c</b></td><td width="57"><b>d</b></td></tr><tr><td><b>反应前的质量/g</b></td><td><b>6.4</b></td><td><b>14.0</b></td><td><b>3.2</b></td><td><b>1.0</b></td></tr><tr><td><b>反应一段时间后的质量/g</b></td><td><b>10.0</b></td><td><b>7.2</b></td><td><b>x</b></td><td><b>1.0</b></td></tr></tbody></table>下列有关说法正确的是（　　）</a></li></ul><ul style="display: none;"><li><a href="http://www.jyeoo.com/chemistry/ques/detail/736631f0-841d-49a1-b3bc-12d47ae047ae" target="_blank"><span class="qseq"></span>（2016•滑县模拟）在一密闭容器中，有甲、乙、丙、丁四种物质，反应前，他们的质量如白色条形图所示．反应结束后，他们的质量如黑色条形图所示．下列说法正确的是（　　）</a></li><li><a href="http://www.jyeoo.com/chemistry/ques/detail/ce44b1b2-4c90-4631-a363-2c50519a8871" target="_blank"><span class="qseq"></span>（2016•重庆校级一模）将a、b、c、d四种物质放入一密闭容器中，在一定条件下发生反应，在不同时刻时四种物质的质量如下，已知a的相对分子质量为d的2倍，下列说法中正确的是（　　） <table class="edittable"><tbody><tr><td width="114">&nbsp;物质</td><td width="114">&nbsp;a</td><td width="114">&nbsp;b</td><td width="114">&nbsp;c</td><td width="114">&nbsp;d</td></tr><tr><td>&nbsp;反应前的质量（g）</td><td>&nbsp;6.4</td><td>&nbsp;1.0</td><td>&nbsp;0.1</td><td>&nbsp;1.6</td></tr><tr><td>&nbsp;t时刻的质量（g）</td><td>&nbsp;3.2</td><td>&nbsp;X</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;反应后的质量（g）</td><td>&nbsp;0</td><td>&nbsp;5.4</td><td>&nbsp;Y</td><td>&nbsp;0</td></tr></tbody></table></a></li><li><a href="http://www.jyeoo.com/chemistry/ques/detail/bcbdee27-57f2-454b-b2f0-d792b26e157d" target="_blank"><span class="qseq"></span>（2016•滑县模拟）2A+3B═C+3D中A和C的相对分子质量比为3：38，D的相对分子质量为2．已知一定量的A和B恰好完全反应，生成34.2gC和0.6gD，则B的相对分子质量为（　　）</a></li><li><a href="http://www.jyeoo.com/chemistry/ques/detail/b516fcd6-dc1e-4b39-9d3e-49fa85809da0" target="_blank"><span class="qseq"></span>（2016秋•东台市期末）密闭容器内有两种物质，在一定条件下充分反应，测得反应前后各物质的质量如表，下列说法正确的是（　　） <table class="edittable"><tbody><tr><td width="114">物质</td><td width="76">X</td><td width="76">Y</td><td width="76">Z</td><td width="76">Q</td></tr><tr><td>反应前质量/g</td><td>8</td><td>2</td><td>20</td><td>5</td></tr><tr><td>反应后质量/g</td><td>待测</td><td>12</td><td>8</td><td>15</td></tr></tbody></table></a></li><li><a href="http://www.jyeoo.com/chemistry/ques/detail/78721dab-7c68-4207-a5ff-f1bd06d41d17" target="_blank"><span class="qseq"></span>（2016•肇源县一模）下列图象不能正确反映其对应操作中各量变化关系的是（　　）</a></li></ul><ul style="display: none;"><li><a href="http://www.jyeoo.com/chemistry/ques/detail/be0cc677-2ec8-4fab-a014-be7259b7315e" target="_blank"><span class="qseq"></span>（2017•罗平县一模）在化学反应前后，下列各项肯定没有变化的是（　　）①原子的种类&nbsp;&nbsp;&nbsp;②物质的总质量&nbsp;&nbsp;③元素的种类&nbsp;&nbsp;&nbsp;④分子的数目&nbsp;&nbsp;&nbsp;⑤物质的种类&nbsp;&nbsp;&nbsp;⑥原子的数目．</a></li><li><a href="http://www.jyeoo.com/chemistry/ques/detail/d340c4ac-6e30-4294-962d-36e63426894e" target="_blank"><span class="qseq"></span>（2016•肥城市模拟）下列对课本中的原理、图表、数据的使用，叙述不正确的是（　　）</a></li><li><a href="http://www.jyeoo.com/chemistry/ques/detail/9adde572-371c-4978-b772-f3fdcabcad25" target="_blank"><span class="qseq"></span>（2017•丰顺县校级模拟）华为公司研发了一种以甲醇为原料的新型手机电池，其容量为锂电池的l0倍，可连续使用1个月才充一次电，其电池反应原理为：2CH<sub>3</sub>OH+3X+4NaOH═2Na<sub>2</sub>CO<sub>3</sub>+6H<sub>2</sub>O．其中X的化学式为（　　）</a></li><li><a href="http://www.jyeoo.com/chemistry/ques/detail/c4d5cded-09db-400d-8666-045b435a8507" target="_blank"><span class="qseq"></span>（2017•丰顺县校级模拟）在化学反应A+2B═C+D中，5.6gA和7.3gB恰好完全反应，生成12.7gC，同时得到D的质量是（　　）</a></li><li><a href="http://www.jyeoo.com/chemistry/ques/detail/fe5eef98-135a-48fe-bf60-ea9324a27015" target="_blank"><span class="qseq"></span>（2017•罗平县一模）一个密闭容器中加入甲、乙、丙、丁四种物质，在一定条件下发生化学反应，测得数据见表．下列说法中不正确的是（　　）<table class="edittable"><tbody><tr><td width="195">物质</td><td width="85">甲</td><td width="83">乙</td><td width="84">丙</td><td width="85">丁</td></tr><tr><td>反应前质量</td><td>8g</td><td>35g</td><td>5g</td><td>8g</td></tr><tr><td>反应后质量</td><td>2g</td><td>X</td><td>5g</td><td>42g</td></tr></tbody></table></a></li></ul><ul style="display: none;"><li><a href="http://www.jyeoo.com/chemistry/ques/detail/ab927f13-37fb-4556-ab3f-6e93089bf5f5" target="_blank"><span class="qseq"></span>（2016•重庆校级三模）密闭容器中有甲、乙两种物质各10g，加热一段时间后测得容器中各物质的质量如表所示<table class="edittable"><tbody><tr><td width="115">物质</td><td width="82">甲</td><td width="86">乙</td><td width="86">丙</td><td width="95">丁</td></tr><tr><td>反应后质量/g</td><td>1.6</td><td>X</td><td>0.9</td><td>2.2</td></tr></tbody></table>下列选项正确的是（　　）</a></li><li><a href="http://www.jyeoo.com/chemistry/ques/detail/8cd96cb9-dfde-48ec-a724-15de3c15266b" target="_blank"><span class="qseq"></span>（2016•湘潭模拟）二甲醚（CH<sub>3</sub>OCH<sub>3</sub>）可由一氧化碳和物质X在一定的条件下制得．反应的化学方程式为2CO+4X═CH<sub>3</sub>OCH<sub>3</sub>+H<sub>2</sub>O，则X的化学式为（　　）</a></li><li><a href="http://www.jyeoo.com/chemistry/ques/detail/e02f5c8b-3e84-4415-809f-084d3f50703b" target="_blank"><span class="qseq"></span>（2016•邹平县模拟）密闭容器内有A、B、C、D四种物质，在一定条件下充分反应，测得反应前后各物质的质量如下：
<table class="edittable">
<tbody>
<tr>
<td width="114">物&nbsp;&nbsp;&nbsp;&nbsp;质</td>
<td width="89">A</td>
<td width="90">B</td>
<td width="91">C</td>
<td width="90">D</td></tr>
<tr>
<td>反应前质量/g</td>
<td>19.7</td>
<td>8.7</td>
<td>31.6</td>
<td>0.4</td></tr>
<tr>
<td>反应后质量/g</td>
<td>待测</td>
<td>17.4</td>
<td>0</td>
<td>3.6</td></tr></tbody></table>下列说法正确的是（　　）</a></li><li><a
href="http://www.jyeoo.com/chemistry/ques/detail/4e35681f-0fed-4fc5-8eae
-4292a2683b4a" target="_blank"><span
class="qseq"></span>（2016•虞城县三模）在由CH<sub>4</sub>和H<sub>2</sub
>组成的混合气体中，测知碳元素的质量分数为60%，则混合气体充分燃烧生成二氧化碳和水的质量比为（　　）</a></li><li><a
href="http://www.jyeoo.com/chemistry/ques/detail/384264d8-8311-447b-bd3d
-384e16e067c6" target="_blank"><span
class="qseq"></span>（2016
•郯城县校级一模）在一密闭容器中，有甲、乙、丙、丁四种物质，在一定条件下存在某个反应，测得反应前后各物质的质量如下表：对该反应，下列描述正确的是（　　）<table class="edittable"><tbody><tr><td width="118">物质</td><td width="70">甲</td><td width="73">乙</td><td width="61">丙</td><td width="61">丁</td></tr><tr><td>反应前物质/g</td><td>20</td><td>m</td><td>20</td><td>20</td></tr><tr><td>反应后物质/g</td><td>2</td><td>待测</td><td>32</td><td>26</td></tr></tbody></table></a></li></ul></div>
            <div class="c20"></div>
            <div class="ques-bottom" id="pchvbe" value="1">
                <div class="c10"></div>
                <table style="width:100%">
                    <tbody><tr>
                        <td style="width:49%;text-align:left;"><div
                        id="ja004" class="fright"></div></td>
                        <td style="width:2%"></td>
                        <td style="width:49%;text-align:left;"><div
                        id="ja006" class="fright"></div></td>
                    </tr>
                </tbody></table>
            </div>
                <div class="ques-comments">
<div id="divComments" style="display:none"><div class="c10"></div><dl
class="discuss" style="padding:0;margin:0;border:1px solid
#ccc"><dt><strong>相关评论</strong></dt><dd style="padding:5px
10px;border-top:1px solid #ccc"><ul><li><span
class="lou"><em>1</em><sup>楼</sup></span><a
href="http://blog.jyeoo.com/193076" target="_blank"><img
src="/api/photo/193076" class="hp" height="22" width="22"
align="absmiddle">193076</a><span class="date">[2013年1月20日
14:26]</span><p>怎么答案和解答不一样 选A嘛 显示的是B 解析是对的</p></li><li><span
class="lou"><em>2</em><sup>楼</sup></span><a
href="http://blog.jyeoo.com/1304179" target="_blank"><img
src="/api/photo/1304179" class="hp" height="22" width="22"
align="absmiddle"><input type="button" class="vip210"
disabled="">起点线</a><span class="date">[2013年1月21日
13:31]</span><p>已经修改，非常感谢，祝您愉快。<br><br>菁优网</p></li></ul></dd></dl></div>
<div class="c10"></div>
<dl class="discuss" style="padding:0;margin:0;border:none;overflow:hidden">
    <dt style="padding:0;margin:0;padding-right:5px"><span class="fright"
    id="spanSummary"><a href="javascript:void(0)" onclick="toggleComments(
    this)">共<span>2</span>条评论，平均得<span>10</span>分（满分为<span>10</span
    >分），点击显示评论</a></span><strong>评论/纠错</strong></dt>
    <dd>
        <div style="margin:4px 0"><textarea id="tbComment"
        style="width:99%;height:90px"></textarea></div>
        <div style="margin:6px 0;color:#555">
            <span style="float:right">
                <input class="btn-box-1" type="button" value="提交"
                onclick="submitComment(false,'chemistry',
                '5518724c-6cc8-4b8d-9d0c-a4c97f4d2440','3')">
            </span>
            <span style="float:left">
                解析质量<label title="思路清晰，解答条理"><input type="radio" value="10"
                name="rbScore" checked="checked">好</label><label
                title="思路较清晰，解答较条理"><input type="radio" value="8"
                name="rbScore">中</label><label title="分析简单，解答模糊或有错误"><input
                type="radio" value="4" name="rbScore">差</label>
            </span>
        </div>
        <div style="clear:both"></div>
    </dd>
</dl>
</div>
        </div>
    </div>
    <div class="c20"></div>
</div>

        </div>
    </div>
    <div class="foot">
        <div style=" width:700px;height:80px;margin:0 auto"><div><a
        target="_blank" href="http://www.jyeoo.com/business"
        rel="nofollow">商务合作</a><em class="m5">|</em><a target="_blank"
        href="http://www.jyeoo.com/home/note" rel="nofollow">服务条款</a><em
        class="m5">|</em><a target="_blank"
        href="http://www.jyeoo.com/home/about" rel="nofollow">关于我们</a><em
        class="m5">|</em><a target="_blank"
        href="http://www.jyeoo.com/support" rel="nofollow">帮助中心</a><em
        class="m5">|</em><a id="aCNZZ" title="菁优网站长统计"
        href="http://www.cnzz.com/stat/website.php?web_id=2018550"
        target="_blank">站长统计</a><script type="text/javascript">$(function(){
        $.getScript('http://s94.cnzz.com/stat.php?id=2018550&web_id=2018550',
        function () { $('#aCNZZ').prop('title', '菁优网站长统计');
        });});</script><em class="m5">|</em><a target="_blank"
        href="http://www.jyeoo.com/home/suggest" rel="nofollow">意见反馈</a><div
        style="clear:both"></div><a target="_blank"
        href="http://www.miibeian.gov.cn/">粤ICP备10006842号</a> <a
        target="_blank" href="http://www.gdca.gov.cn/">粤B2-20100319</a>
        &nbsp;©2010-2017&nbsp;&nbsp;jyeoo.com，V2.21719</div></div>

    </div>
    <div id="divMsg" style="display:none; z-index:6001;"></div>
    <a title="返回顶部" class="return-top" style="right: 30px; position: fixed;
    display: block; bottom: 30px; z-index: 2147483647;" href="#"></a>
    <script type="text/javascript">
        $(function () {
            starCheckMessage();

            initLayout('qb');

            _checkBrowser();

            remind_check();

            var sf = $("#searchform"), sq = "";
            if (sq == "") {
                sq = $.cookie('jye_search_q');
            }

            sf.find("form").submit(function () { var v = $("#qb", sf).val();
            if (!/[0-9a-z\u4E00-\u9FA5]/ig.test(v)) { alert("请输入正确的查询内容！");
            return false; } if (v.length > 100) { $("#qb", sf).val(v.substr(
            0, 99)); } return true; });

            $('.search-ques', sf).hover(function () { $('.dropdown-menu',
            sf).show(); }, function () { $('.dropdown-menu', sf).hide(); });

            if (sq) { $('a[data-sq=' + sq + ']', sf).click(); }

            $(".quesborder,.JYE_MATH_SELECTOR").each(function () {
                try {
                    renderLatex(this);
                } catch (e) { }
            });
        });
        function openLoginUI(u, o, t) { _openLoginUI("chemistry", u, o, t); }
        function openAnalyze(i, t) { _openAnalyze("chemistry", i, t); }
        function _setc(el) {
            el = $(el);

            var fm = el.closest('form'), sq = el.data('sq'), ph = el.data('ph');

            $('#c', fm).val(sq);
            $('#qb', fm).prop('placeholder', ph);
            $('em', fm).text(el.text());

            $('.dropdown-menu', fm).css({ 'display': 'none' });

            $.cookie('jye_search_q', sq);
        }
        function _checkBrowser() {
            try {
                if (navigator.userAgent.toLowerCase().indexOf('chrome') > -1) {
                    var desc = navigator.mimeTypes[
                    'application/x-shockwave-flash'].description.toLowerCase();
                    if (desc.indexOf('adobe') > -1 ||
                    navigator.appVersion.indexOf('UBrowser') > -1) {
                        $("#borwserWarning").animate({ "height": "show" });
                        setTimeout(_closeWarning, 2000);
                        return;
                    }
                    var mimeType = navigator.mimeTypes;
                    for (var i = 0 ; i < mimeType.length; i++) {
                        if (mimeType[i]['type'].indexOf('sogou') > -1) {
                            $("#borwserWarning").animate({ "height": "show" });
                            setTimeout(_closeWarning, 2000);
                            break;
                        }
                    }
                }
            } catch (e) {
                return;
            }
        }
        function _closeWarning() {
            $("#borwserWarning").animate({ "height": "hide" });
        }

        function _rs(el) {
            el = $(el);

            var u = window.location.href.toLowerCase(), pa = el.data('pa'),
            pv = el.data('pv');
            if (!pv) {
                pv = el.val();
            }

            var apa = pa.toString().split(','), apv = pv.toString().split(',');
            for (var i = 0; i < apa.length; i++) {
                u = _url(u, apa[i], apv[i]);
            }

            window.location.href = u;
        }

        function _url(u, pa, pv) {
            var i = u.indexOf('?');

            if (i == -1) {
                u += '?' + encodeURIComponent(pa) + '=' + encodeURIComponent(
                pv);
            } else {
                var qp = new QP(u);

                u = u.substring(0, i) + '?' + encodeURIComponent(pa) + '=' +
                encodeURIComponent(pv);

                for (var ia in qp) {
                    if (ia != pa) {
                        u += '&' + encodeURIComponent(ia) + '=' +
                        encodeURIComponent(qp[ia]);
                    }
                }
            }

            return u;
        }

        function _findCampusData(data, id) {
            for (var i = 0; i < data.length; i++) {
                if (data[i].Key == id) {
                    return data[i];
                }
            }
            return null;
        }
        function _initCampusQues(subject, ids) {
            $.post('/' + subject + '/ques/checkcampusques', { 'a':
            JSON.stringify(ids), 'r': Math.random() }, function (data) {
                if (data) {
                    if (data.S == 0) {
                        $(ids).each(function () {
                            var qid = this, span = $('#' + qid).next(
                            "span.fieldtip");
                            if (span.size() == 1) {
                                var cq = _findCampusData(data.D, qid);
                                if (cq == null) {
                                    $("<a href=\"javascript:void(0)\"
                                    title=\"点击将把本题加入或移出校本题库\"
                                    onclick=\"_actionCampusQues(this,
                                    '" + subject + "','" + qid + "')\"
                                    class='btn-ui
                                    add3'>加入校本题库</a>").appendTo(span);
                                } else if (cq.Value == 2) {
                                    $("<a href=\"javascript:void(0)\"
                                    class='btn-ui
                                    pri3'>校本私密试题</a>").appendTo(span);
                                } else {
                                    $("<a href=\"javascript:void(0)\"
                                    title=\"点击将把本题加入或移出校本题库\"
                                    onclick=\"_actionCampusQues(this,
                                    '" + subject + "','" + qid + "')\"
                                    class='btn-ui
                                    del3'>移出校本题库</a>").appendTo(span);
                                }
                            }
                        });
                    }
                }
            });
        }
        function _actionCampusQues(el, subject, id) {
            el = $(el);
            $.post('/' + subject + '/ques/actioncampusques', { 'id': id,
            'r': Math.random() }, function (data) {
                if (data) {
                    if (data.S == 0) {
                        if (el.hasClass("add3")) {
                            el.removeClass("add3").addClass('del3').html(
                            "移出校本题库");
                        } else {
                            el.removeClass("del3").addClass('add3').html(
                            "加入校本题库");
                        }
                        showMessage(data.M);
                    } else {
                        showMessage(data.M, false);
                    }
                }
            });
        }

        function _initCampusReport(subject, ids) {
            $.post('/' + subject + '/report/checkcampusreport', { 'a':
            JSON.stringify(ids), 'r': Math.random() }, function (data) {
                if (data) {
                    if (data.S == 0) {
                        $(ids).each(function () {
                            var qid = this, span = $('#' + qid);
                            if (span.size() == 1) {
                                var cq = _findCampusData(data.D, qid);
                                if (cq == null) {
                                    $("<a href=\"javascript:void(0)\"
                                    title=\"点击将把本卷加入或移出校本卷库\"
                                    onclick=\"_actionCampusReport(this,
                                    '" + subject + "','" + qid + "')\"
                                    class='btn-ui
                                    add3'>加入校本卷库</a>").appendTo(span);
                                } else if (cq.Value == 2) {
                                    $("<a href=\"javascript:void(0)\"
                                    class='btn-ui
                                    pri3'>校本私密试卷</a>").appendTo(span);
                                } else {
                                    $("<a href=\"javascript:void(0)\"
                                    title=\"点击将把本卷加入或移出校本卷库\"
                                    onclick=\"_actionCampusReport(this,
                                    '" + subject + "','" + qid + "')\"
                                    class='btn-ui
                                    del3'>移出校本卷库</a>").appendTo(span);
                                }
                            }
                        });
                    }
                }
            });
        }
        function _actionCampusReport(el, subject, id) {
            el = $(el);
            $.post('/' + subject + '/report/actioncampusreport', { 'id': id,
            'r': Math.random() }, function (data) {
                if (data) {
                    if (data.S == 0) {
                        if (el.hasClass("add3")) {
                            el.removeClass("add3").addClass('del3').html(
                            "移出校本卷库");
                        } else {
                            el.removeClass("del3").addClass('add3').html(
                            "加入校本卷库");
                        }
                        showMessage(data.M);
                    } else {
                        showMessage(data.M, false);
                    }
                }
            });
        }
    </script>

    <script type="text/javascript">
        $(function () {
            QuesCart.init("chemistry", true);

            var nav = $(".nav"), navTop = nav.offset().top, divL = $(
            '.detail-right'); divLTop = divL.offset().top;
            getQuesData('chemistry', '5518724c-6cc8-4b8d-9d0c-a4c97f4d2440',
            1, function (data) { if (data.S == 0) { for (var i = 0; i <
            data.D.length; i++) { $(data.D[i]).appendTo('.ques-related'); }
            $('.ques-related').each(function () { renderLatex(this); }); $(
            '.qtitle > a').each(function (i, el) { $(el).hover(function () {
            showRelated(i); }); }); showRelated(0); } }, function () { },
            function () { });
            getQuesData('chemistry', '5518724c-6cc8-4b8d-9d0c-a4c97f4d2440',
            2, function (data) { if (data.S == 0) { $(data.D[0]).appendTo(
            '.ques-reports'); } if ($('.ques-reports').children('ul').size()
            == 0) { $('.ques-reports').hide(); } }, function () { }, function
            () { });
            getQuesData('chemistry', '5518724c-6cc8-4b8d-9d0c-a4c97f4d2440',
            3, function (data) { if (data.S == 0) { if (data.D[1] > 0) { $(
            '<a href="javascript:void(0)" onclick="toggleComments(this)">' +
            data.D[2] + '，点击显示评论</a>').appendTo('#spanSummary'); $(data.D[
            0]).appendTo('#divComments'); } } }, function () { }, function ()
            { });

            $('.jwaudio').JyeAudio();

            $(window).scroll(function () {
                var s = $(document).scrollTop();

                if ($(window).height() >= 650 && s > divLTop) {
                    if (!divL.hasClass('tree-box-show')) {
                        divL.css({ "left": divL.offset().left }).addClass(
                        'tree-box-show');
                    }
                }
                else {
                    divL.removeClass('tree-box-show');
                }

                if ($(window).height() >= 650 && s > navTop) {
                    if (!nav.hasClass('nav-box-show')) {
                        nav.addClass('nav-box-show')
                    }
                }
                else {
                    nav.removeClass('nav-box-show')
                }
            });
        });
        function showRelated(i) {
            $('.qtitle > a').removeClass('cur').eq(i).addClass('cur');
            $('.ques-related > ul').hide().eq(i).show();
        }
        function adCallback() {
            if ($('#ja011').children().size() > 0) { $('.ques-videos').show(); }
            if ($('#ja004').children().size() > 0) { $('.ques-bottom').show(); }
            if ($('#ja035').children().size() == 0) {
                $('<ul><li><a href="http://xyh.jyeoo.com/home/join#3"
                target="_blank" onclick="return openCampusForm(
                this)">您附近还没有教育机构加入校园号，立即加入校园号</a></li></ul>').appendTo($(
                '#ja035'));
            } else {
                $('<a href="http://xyh.jyeoo.com/home/join#3" target="_blank"
                class="fright" onclick="return openCampusForm(
                this)">+我也要加入</a>').appendTo($('#ja035'));
            }
            $('.ques-xyh').show();
        }
        function refreshMe() { }
        function commentMe() { window.location.href =
        "http://www.jyeoo.com/chemistry/ques/detail/5518724c-6cc8-4b8d-9d0c
        -a4c97f4d2440"; }
        function loginCallback() { if ($.trim($("#tbComment").val()).length >
        0) { postComment("chemistry", "5518724c-6cc8-4b8d-9d0c-a4c97f4d2440",
        "3"); } else { detailRefresh(); } }
        function detailRefresh() { window.location.href =
        "http://www.jyeoo.com/chemistry/ques/detail/5518724c-6cc8-4b8d-9d0c
        -a4c97f4d2440"; }

        function getQuesData(sb, id, tp, fs, ff, fd) {
            $.getJSON('/' + sb + '/api/getquesdata/' + id + '?a=' + tp +
            '&r=' + Math.random(), function (r) { fs(r); }).fail(function (
            xhr, status, err) { ff(xhr, status, err); }).done(function () {
            fd(); });
        }
    </script>
    <script type="text/javascript"
    src="http://a.jyeoo.com/js?sb=22&amp;pt=G1&amp;cb=adCallback&amp;ps=9
    %2c11%2c31%2c33%2c35%2c4%2c6%2c46" async="async" defer="defer"></script>


<div id="JYE_AUDIO_JWPLAYER_wrapper" style="position: relative; width: 0px;
height: 0px;"><object type="application/x-shockwave-flash"
data="http://img.jyeoo.net//jwplayer/player.swf" width="100%" height="100%"
bgcolor="#000000" id="JYE_AUDIO_JWPLAYER" name="JYE_AUDIO_JWPLAYER"
tabindex="0"><param name="allowfullscreen" value="true"><param
name="allowscriptaccess" value="always"><param name="seamlesstabbing"
value="true"><param name="wmode" value="opaque"><param name="flashvars"
value="netstreambasepath=http%3A%2F%2Fwww.jyeoo.com%2Fchemistry%2Fques
%2Fdetail%2F5518724c-6cc8-4b8d-9d0c-a4c97f4d2440&amp;id=JYE_AUDIO_JWPLAYER
&amp;controlbar.position=over"></object></div></body>"""


def test_re(re_express):
    partern = re.compile(re_express)
    partern.findall(test_html)
    for group in partern.groups:
        for data_str in group:
            print data_str
