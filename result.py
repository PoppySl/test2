# import glob
# from PIL import Image
# file = "sample/image/*"
# for i in glob.glob(file):
#     print(i)
#     imagefile = i.split('.')
#     imageName = imagefile[0][-5:]
#     print(imageName)
#     image = Image.open(i)
#     image = image.crop((0, 0, 110, 20))
#     img = image.convert('RGBA')
#     img.save("sample/new_train/%s.png" % imageName, 'PNG')


from pyquery import PyQuery as pq

htmlTrue = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>監理服務網行動版-交通違規罰鍰查詢</title>
<meta name=viewport content="width=device-width, initial-scale=0.5">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
<meta http-equiv="Pragma" content="no-cache" />
<meta http-equiv="Cache-Control" content="no-cache" />
<meta http-equiv="Expires" content="0" />
<link href="/m3/css/mobo/style.css" rel="stylesheet" type="text/css"/>
</head>
<body>
<!-- header start -->

<div id="top_banner">
	<div id="top_bt01"><a href="/?from=mobile"><img src="/m3/images/mobo/bt17.png" width="100%" style="padding:0;"/></a></div>
</div>
<div id="top_banner"><img src="/m3/images/mobo/top_banner.png" width="100%" /></div>
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="padding:0">
  <tr>
    <td width="33.333%">
    <a href="car">
    
    
    <img src="/m3/images/mobo/top_bt01-1.png" width="100%" />
    
    </a>
    </td>
    <td width="33.333%">
    <a href="moboTrafficFine">
    
    <img src="/m3/images/mobo/top_bt02.png" width="100%" />
    
    
    
    </a>
    </td>
     <td width="33.333%">
    <a href="service">
    
    
    <img src="/m3/images/mobo/top_bt04-1.png" width="100%" />
    
    
    </a>
    </td>
  </tr>
</table>

<!-- header end -->
<center><p class=index_title>交通違規罰鍰查詢</p></center>
<div class="irregularities_data02"><img src="/m3/images/mobo/banner01.png" width="100%" /></div>
<div class="irregularities_data"><span class="rose_text02">23****44</span> ，可線上繳費的違規紀錄共<span class="rose_text02">529</span>筆，紀錄如下：</div>
 
 <form action="moboTrafficFinePay"method="post" id="trafficFinePay">
   
<div class="irregularities_data01">
  <div><table width="100%" border="0" cellspacing="2" cellpadding="5" class="irregularities_table01">
  <tr>
    <td width="10%" rowspan="4" align="center" bgcolor="#FFFFFF">
    
    
    
     <input class="input_type" name="tfid[]" id="tf_id3" type="checkbox" value="3" 
      onclick="changePay('3','Tue May 05 10:06:00 CST 2020','在公共汽車招呼站十公尺內停車                                                                                                                                                                                                      ','0','Thu Jun 25 00:00:00 CST 2020',
      '1AL634409  ','RBQ-8316','1200','v','復興南路一段                                                                        ','20','22 ')" />
    
    
     </td>
    <td width="28%" bgcolor="#F5F5F5">違規日</td>
    <td bgcolor="#FFFFFF">109.05.05</td>
  </tr>
  <tr>
    <td width="28%" bgcolor="#F5F5F5">事由</td>
    <td bgcolor="#FFFFFF">在公共汽車招呼站十公尺內停車                                                                                                                                                                                                      </td>
  </tr>
  <tr>
    <td width="28%" bgcolor="#F5F5F5">罰鍰</td>
    <td bgcolor="#FFFFFF">1200元</td>
  </tr>
  <tr>
    <td width="28%" bgcolor="#F5F5F5">應到案日</td>
     
    <td bgcolor="#FFFFFF">109.06.25</td>
    
  </tr>
  
</table>
</div>
</div>

<div class="irregularities_data01">
  <div><table width="100%" border="0" cellspacing="2" cellpadding="5" class="irregularities_table01">
  <tr>
    <td width="10%" rowspan="4" align="center" bgcolor="#FFFFFF">
    
    
    
     <input class="input_type" name="tfid[]" id="tf_id2" type="checkbox" value="2" 
      onclick="changePay('2','Tue May 05 14:52:00 CST 2020','在禁止臨時停車處所停車                                                                                                                                                                                                               ','0','Thu Jun 25 00:00:00 CST 2020',
      '1AL634881  ','RCK-0673','900','v','復興北路                                                                              ','20','22 ')" />
    
    
     </td>
    <td width="28%" bgcolor="#F5F5F5">違規日</td>
    <td bgcolor="#FFFFFF">109.05.05</td>
  </tr>
  <tr>
    <td width="28%" bgcolor="#F5F5F5">事由</td>
    <td bgcolor="#FFFFFF">在禁止臨時停車處所停車                                                                                                                                                                                                               </td>
  </tr>
  <tr>
    <td width="28%" bgcolor="#F5F5F5">罰鍰</td>
    <td bgcolor="#FFFFFF">900元</td>
  </tr>
  <tr>
    <td width="28%" bgcolor="#F5F5F5">應到案日</td>
     
    <td bgcolor="#FFFFFF">109.06.25</td>
    
  </tr>
  
</table>
</div>
</div>

<div class="irregularities_data01">
  <div><table width="100%" border="0" cellspacing="2" cellpadding="5" class="irregularities_table01">
  <tr>
    <td width="10%" rowspan="4" align="center" bgcolor="#FFFFFF">
    
    
    
     <input class="input_type" name="tfid[]" id="tf_id1" type="checkbox" value="1" 
      onclick="changePay('1','Thu May 07 11:31:00 CST 2020','汽車駕駛人行車速度，超過規定之最高時速20公里以內                                                                                                                                                                         ','0','Mon Jun 22 00:00:00 CST 2020',
      'BID132163  ','RCD-8736','1600','a','三多一路，武營路西向東約200公尺       ','20','22 ')" />
    
    
     </td>
    <td width="28%" bgcolor="#F5F5F5">違規日</td>
    <td bgcolor="#FFFFFF">109.05.07</td>
  </tr>
  <tr>
    <td width="28%" bgcolor="#F5F5F5">事由</td>
    <td bgcolor="#FFFFFF">汽車駕駛人行車速度，超過規定之最高時速20公里以內                                                                                                                                                                         </td>
  </tr>
  <tr>
    <td width="28%" bgcolor="#F5F5F5">罰鍰</td>
    <td bgcolor="#FFFFFF">1600元</td>
  </tr>
  <tr>
    <td width="28%" bgcolor="#F5F5F5">應到案日</td>
     
    <td bgcolor="#FFFFFF">109.06.22</td>
    
  </tr>
  
</table>
</div>
</div>

<div class="irregularities_data01">
  <div><table width="100%" border="0" cellspacing="2" cellpadding="5" class="irregularities_table01">
  <tr>
    <td width="10%" rowspan="4" align="center" bgcolor="#FFFFFF">
    
    
    
     <input class="input_type" name="tfid[]" id="tf_id6" type="checkbox" value="6" 
      onclick="changePay('6','Sun May 03 14:10:00 CST 2020','在禁止臨時停車處所停車                                                                                                                                                                                                               ','0','Mon Jun 22 00:00:00 CST 2020',
      'A01S891A7  ','RCP-3187','900','v','行善路                                                                                 ','20','22 ')" />
    
    
     </td>
    <td width="28%" bgcolor="#F5F5F5">違規日</td>
    <td bgcolor="#FFFFFF">109.05.03</td>
  </tr>
  <tr>
    <td width="28%" bgcolor="#F5F5F5">事由</td>
    <td bgcolor="#FFFFFF">在禁止臨時停車處所停車                                                                                                                                                                                                               </td>
  </tr>
  <tr>
    <td width="28%" bgcolor="#F5F5F5">罰鍰</td>
    <td bgcolor="#FFFFFF">900元</td>
  </tr>
  <tr>
    <td width="28%" bgcolor="#F5F5F5">應到案日</td>
     
    <td bgcolor="#FFFFFF">109.06.22</td>
    
  </tr>
  
</table>
</div>
</div>

<div class="irregularities_data01">
  <div><table width="100%" border="0" cellspacing="2" cellpadding="5" class="irregularities_table01">
  <tr>
    <td width="10%" rowspan="4" align="center" bgcolor="#FFFFFF">
    
    
    
     <input class="input_type" name="tfid[]" id="tf_id5" type="checkbox" value="5" 
      onclick="changePay('5','Sun May 03 16:08:00 CST 2020','在禁止臨時停車處所停車                                                                                                                                                                                                               ','0','Mon Jun 22 00:00:00 CST 2020',
      'A00ZN69A2  ','RCA-5350','900','v','忠孝東路六段                                                                        ','20','22 ')" />
    
    
     </td>
    <td width="28%" bgcolor="#F5F5F5">違規日</td>
    <td bgcolor="#FFFFFF">109.05.03</td>
  </tr>
  <tr>
    <td width="28%" bgcolor="#F5F5F5">事由</td>
    <td bgcolor="#FFFFFF">在禁止臨時停車處所停車                                                                                                                                                                                                               </td>
  </tr>
  <tr>
    <td width="28%" bgcolor="#F5F5F5">罰鍰</td>
    <td bgcolor="#FFFFFF">900元</td>
  </tr>
  <tr>
    <td width="28%" bgcolor="#F5F5F5">應到案日</td>
     
    <td bgcolor="#FFFFFF">109.06.22</td>
    
  </tr>
  
</table>
</div>
</div>

<div class="irregularities_data01">
  <div><table width="100%" border="0" cellspacing="2" cellpadding="5" class="irregularities_table01">
  <tr>
    <td width="10%" rowspan="4" align="center" bgcolor="#FFFFFF">
    
    
    
     <input class="input_type" name="tfid[]" id="tf_id4" type="checkbox" value="4" 
      onclick="changePay('4','Sun May 03 17:36:00 CST 2020','轉彎或變換車道不依標誌、標線、號誌指示                                                                                                                                                                                       ','0','Wed Jun 17 00:00:00 CST 2020',
      'BJD235849  ','RCK-1590','600','a','自由、大中                                     ','20','22 ')" />
    
    
     </td>
    <td width="28%" bgcolor="#F5F5F5">違規日</td>
    <td bgcolor="#FFFFFF">109.05.03</td>
  </tr>
  <tr>
    <td width="28%" bgcolor="#F5F5F5">事由</td>
    <td bgcolor="#FFFFFF">轉彎或變換車道不依標誌、標線、號誌指示                                                                                                                                                                                       </td>
  </tr>
  <tr>
    <td width="28%" bgcolor="#F5F5F5">罰鍰</td>
    <td bgcolor="#FFFFFF">600元</td>
  </tr>
  <tr>
    <td width="28%" bgcolor="#F5F5F5">應到案日</td>
     
    <td bgcolor="#FFFFFF">109.06.17</td>
    
  </tr>
  
</table>
</div>
</div>

<input type="hidden" name="searchID"value="23892144"/>

<input type="hidden" name="queryType"value="1"/>
</form>

<!--按鈕-->

<div class="bt01">
<form id="more" action="moboTrafficFineResult" method="post">
<input type="hidden" name="thisPage"value="2"/>
<input type="hidden" name="birthYear"value=""/>
<input type="hidden" name="birthMonth"value=""/>
<input type="hidden" name="birthDay"value=""/>
<input type="hidden" name="searchID"value="23892144"/>
<input type="hidden" name="queryType"value="1"/>
<input type="hidden" name="isPay"value="1"/>
<input type="hidden" name="hasValidateCode"value="1"/>
<a href="javascript:void(0);" onclick="formSubmit('more')">
<img src="/m3/images/mobo/bt05.png" width="100%" /></a>
</form>
</div>

<div class="bt01"><table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td align="left">
    <a href="moboTrafficFineOther">
    <img src="/m3/images/mobo/bt07.png" width="95%" /></a>
    </td>
    <td align="right">
    <form id="payItems"action="moboTrafficFineResult" method="post">
    <input type="hidden" name="thisPage"value="1"/>
    <input type="hidden" name="birthYear"value=""/>
    <input type="hidden" name="birthMonth"value=""/>
    <input type="hidden" name="birthDay"value=""/>
    <input type="hidden" name="searchID"value="23892144"/>
    <input type="hidden" name="queryType"value="1"/>
    <input type="hidden" name="isPay"value="0"/>
    <input type="hidden" name="hasValidateCode"value="1"/>
    <a href="javascript:void(0);" onclick="formSubmit('payItems')">
    <img src="/m3/images/mobo/bt08.png" width="95%" /></a>
    </form>
    </td>
  </tr>
  </table>
</div>

<div class="bt01">
 <a href="javascript:void(0);" onclick="formSubmit('trafficFinePay')">
<img src="/m3/images/mobo/bt09.png" width="100%" /></a></div>
<!--注意事項-->
<div id="notice">
<div class="link_text03" id="moboTitle">注意事項</div>
<div class="note" id="moboNotice">這裡可以打注意事項，這裡可以打注意事項，這裡可以打注意事項，這裡可以打注意事項，這裡可以打注意事項</div></div>
<!-- footer start -->
<div id="footer">地址：10863臺北市萬華區東園街65號<br />
總機：(02)2307-0123(代表號)  監理及大客車投訴專線：0800-231035<br/>  系統操作服務專線0800-080-412(由網站建置廠商中華電信客服提供服務) <br />
  交通部公路總局 版權所有<br/>
  如有監理業務疑問請向<a href="/m3-emv/news/office"><span class="link_text01">全國各監理機關</span></a>洽詢</div>
<!-- footer end -->
<script type="text/javascript" src="/m3/scripts/jquery-latest.min.js"></script>
<script type="text/javascript"
	src="/m3/scripts/jquery-ui-1.10.1.custom.js"></script>
<script type="text/javascript" src="/m3/scripts/function_phase2.js"></script>
<!-- google analytics -->
<script language="javascript" src="/m3/scripts/mvdis_tracking.js"></script>
<script>
$(document).ready(function() {

	noticeSet("moboTrafficFin.js","moboTitle","moboTitle");
	noticeSet("moboTrafficFin.js","moboNotice","moboNotice");
	
});
</script>
<script type="text/javascript">
function changePay(items, vilDate, vilFact, penaltyAmount, arrivedDate,
			vilTicket, plateNo, penalty,respTp,location,dmv,adjNo) {
		var jsonUrl = "/m3-emv-mobo/public/moboTrafficFinePay?method=changePay";

		$.ajax({
			url : jsonUrl,
			type : "POST",
			data : {
				'items' : items,
				'vilDate' : vilDate,
				'vilFact' : vilFact,
				'penaltyAmount' : penaltyAmount,
				'arrivedDate' : arrivedDate,
				'vilTicket' : vilTicket,
				'plateNo' : plateNo,
				'penalty' : penalty,
				'respTp' : respTp,
				'location' : location,
				'dmv' : dmv,
				'adjNo' : adjNo
			},
			dataType : 'html',
			cache : false,
			success : function(data, textStatus, XMLHttpRequest) {

			},
			error : function(xhr, ajaxOptions, thrownError) {
				alert("資料傳輸發生錯誤：" + xhr.statusText + thrownError);
				setTimeout(function() {
					closeShowMsg();
				}, 2000);
			}
		});
	}
	</script>


</body>
</html>'''

html = '''
<html xmlns="http://www.w3.org/1999/xhtml" xmlns="http://www.w3.org/1999/xhtml">&#13;
<head>&#13;
<title>監理服務網行動版-交通違規罰鍰查詢</title>&#13;
<meta name="viewport" content="width=device-width, initial-scale=0.5" />&#13;
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />&#13;
<meta http-equiv="Pragma" content="no-cache" />&#13;
<meta http-equiv="Cache-Control" content="no-cache" />&#13;
<meta http-equiv="Expires" content="0" />&#13;
<link href="/m3/css/mobo/style.css" rel="stylesheet" type="text/css" />&#13;
<script type="text/javascript" src="/m3/scripts/jquery-latest.min.js"></script>&#13;
<script type="text/javascript" src="/m3/scripts/jquery-ui-1.10.1.custom.js"></script>&#13;
<script type="text/javascript" src="/m3/scripts/function_phase2.js"></script>&#13;
<!-- google analytics -->&#13;
<script language="javascript" src="/m3/scripts/mvdis_tracking.js"></script>&#13;
<script>&#13;
$(document).ready(function() {&#13;
	noticeSet("moboTrafficFin.js","N","wrong");&#13;
	noticeSet("moboTrafficFin.js","moboTitle","moboTitle");&#13;
	noticeSet("moboTrafficFin.js","moboNotice","moboNotice");&#13;
	&#13;
});&#13;
&#13;
</script>&#13;
<script>alert("驗證碼不存在！");</script>&#13;
&#13;
<script>&#13;
var browser = {&#13;
 versions: function () {&#13;
  var u = navigator.userAgent, app = navigator.appVersion;&#13;
  return {   &#13;
   trident: u.indexOf('Trident') &gt; -1, &#13;
   presto: u.indexOf('Presto') &gt; -1, &#13;
   webKit: u.indexOf('AppleWebKit') &gt; -1, &#13;
   gecko: u.indexOf('Gecko') &gt; -1 &amp;&amp; u.indexOf('KHTML') == -1, &#13;
   mobile: !!u.match(/AppleWebKit.*Mobile.*/), &#13;
   ios: !!u.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/), &#13;
   android: u.indexOf('Android') &gt; -1 || u.indexOf('Linux') &gt; -1,&#13;
   iPhone: u.indexOf('iPhone') &gt; -1, &#13;
   iPad: u.indexOf('iPad') &gt; -1,&#13;
   webApp: u.indexOf('Safari') == -1 &#13;
  };&#13;
 }(),&#13;
 language: (navigator.browserLanguage || navigator.language).toLowerCase()&#13;
}&#13;
&#13;
var isMobile = '';&#13;
&#13;
console.log('isMobile=' + isMobile);&#13;
&#13;
if(isMobile != 'yes'){&#13;
  if (browser.versions.mobile) {&#13;
    //行動設備瀏覽&#13;
	  console.log('## mobile');&#13;
  } else {&#13;
	  console.log('## pc');&#13;
    //pc&#13;
    window.location = 'https://www.mvdis.gov.tw/m3-emv-vil/vil/penaltyQueryPay?from=mobile';&#13;
  }&#13;
}&#13;
</script>&#13;
</head>&#13;
&#13;
<body>&#13;
<!-- header start -->&#13;
&#13;
<div id="top_banner">&#13;
	<div id="top_bt01"><a href="/?from=mobile"><img src="/m3/images/mobo/bt17.png" width="100%" style="padding:0;" /></a></div>&#13;
</div>&#13;
<div id="top_banner"><img src="/m3/images/mobo/top_banner.png" width="100%" /></div>&#13;
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="padding:0">&#13;
  <tr>&#13;
    <td width="33.333%">&#13;
    <a href="car">&#13;
    &#13;
    &#13;
    <img src="/m3/images/mobo/top_bt01-1.png" width="100%" />&#13;
    &#13;
    </a>&#13;
    </td>&#13;
    <td width="33.333%">&#13;
    <a href="moboTrafficFine">&#13;
    &#13;
    <img src="/m3/images/mobo/top_bt02.png" width="100%" />&#13;
    &#13;
    &#13;
    &#13;
    </a>&#13;
    </td>&#13;
     <td width="33.333%">&#13;
    <a href="service">&#13;
    &#13;
    &#13;
    <img src="/m3/images/mobo/top_bt04-1.png" width="100%" />&#13;
    &#13;
    &#13;
    </a>&#13;
    </td>&#13;
  </tr>&#13;
</table>&#13;
&#13;
<!-- header end -->&#13;
<center><p class="index_title">交通違規罰鍰查詢</p></center>&#13;
<div class="irregularities_red"><table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">&#13;
  <tr>&#13;
    <td width="24%" align="center"><img src="/m3/images/mobo/icon-01.png" width="70%" /></td>&#13;
    <td width="66%" id="wrong">交通違規紀錄不會即時更新，需待8-14天後，才可於線上查詢到。您可以使用<span class="link_text02">簡訊訂閱服務</span>，系統將主動寄發簡訊通知。</td>&#13;
  </tr>&#13;
  </table>&#13;
</div>&#13;
<!-- 查詢表單:個人 Start -->&#13;
 <div id="person">&#13;
<div class="irregularities_top">&#13;
&#13;
<table width="100%" border="0" cellspacing="0" cellpadding="0">&#13;
  <tr>&#13;
    <td valign="bottom" width="33%"><img src="/m3/images/mobo/icon-02.png" width="100%" /></td>&#13;
    <td valign="bottom" width="33%"><a href="javascript:void(0);" onclick="changeDisplay('person','company')"><img src="/m3/images/mobo/icon-03.png" width="100%" /></a></td>&#13;
    <td valign="bottom" width="34%"><img src="/m3/images/mobo/icon-04.png" width="101%" /></td>&#13;
  </tr>&#13;
  </table>&#13;
  <form action="moboTrafficFineResult" method="post" id="personSubmit">&#13;
  <div class="irregularities_main"><table width="95%" border="0" align="center" cellpadding="0" cellspacing="0">&#13;
  <tr>&#13;
    <td>身分證字號：</td>&#13;
    </tr>&#13;
  <tr>&#13;
    <td><input name="searchID" type="text" class="id_nb1" id="txtVerify" maxlength="10" autocomplete="off" /></td>&#13;
    </tr>&#13;
  <tr>&#13;
    <td>生日：</td>&#13;
    </tr>&#13;
  <tr>&#13;
    <td><table width="100%" border="0" cellspacing="0" cellpadding="0">&#13;
      <tr>&#13;
        <td width="25%"><select name="birthYear" class="id_nb1" id="select">&#13;
         &#13;
            <option value="09">9</option>&#13;
		 &#13;
            <option value="010">10</option>&#13;
		 &#13;
            <option value="011">11</option>&#13;
		 &#13;
            <option value="012">12</option>&#13;
		 &#13;
            <option value="013">13</option>&#13;
		 &#13;
            <option value="014">14</option>&#13;
		 &#13;
            <option value="015">15</option>&#13;
		 &#13;
            <option value="016">16</option>&#13;
		 &#13;
            <option value="017">17</option>&#13;
		 &#13;
            <option value="018">18</option>&#13;
		 &#13;
            <option value="019">19</option>&#13;
		 &#13;
            <option value="020">20</option>&#13;
		 &#13;
            <option value="021">21</option>&#13;
		 &#13;
            <option value="022">22</option>&#13;
		 &#13;
            <option value="023">23</option>&#13;
		 &#13;
            <option value="024">24</option>&#13;
		 &#13;
            <option value="025">25</option>&#13;
		 &#13;
            <option value="026">26</option>&#13;
		 &#13;
            <option value="027">27</option>&#13;
		 &#13;
            <option value="028">28</option>&#13;
		 &#13;
            <option value="029">29</option>&#13;
		 &#13;
            <option value="030">30</option>&#13;
		 &#13;
            <option value="031">31</option>&#13;
		 &#13;
            <option value="032">32</option>&#13;
		 &#13;
            <option value="033">33</option>&#13;
		 &#13;
            <option value="034">34</option>&#13;
		 &#13;
            <option value="035">35</option>&#13;
		 &#13;
            <option value="036">36</option>&#13;
		 &#13;
            <option value="037">37</option>&#13;
		 &#13;
            <option value="038">38</option>&#13;
		 &#13;
            <option value="039">39</option>&#13;
		 &#13;
            <option value="040">40</option>&#13;
		 &#13;
            <option value="041">41</option>&#13;
		 &#13;
            <option value="042">42</option>&#13;
		 &#13;
            <option value="043">43</option>&#13;
		 &#13;
            <option value="044">44</option>&#13;
		 &#13;
            <option value="045">45</option>&#13;
		 &#13;
            <option value="046">46</option>&#13;
		 &#13;
            <option value="047">47</option>&#13;
		 &#13;
            <option value="048">48</option>&#13;
		 &#13;
            <option value="049">49</option>&#13;
		 &#13;
            <option value="050">50</option>&#13;
		 &#13;
            <option value="051">51</option>&#13;
		 &#13;
            <option value="052">52</option>&#13;
		 &#13;
            <option value="053">53</option>&#13;
		 &#13;
            <option value="054">54</option>&#13;
		 &#13;
            <option value="055">55</option>&#13;
		 &#13;
            <option value="056">56</option>&#13;
		 &#13;
            <option value="057">57</option>&#13;
		 &#13;
            <option value="058">58</option>&#13;
		 &#13;
            <option value="059">59</option>&#13;
		 &#13;
            <option value="060">60</option>&#13;
		 &#13;
            <option value="061">61</option>&#13;
		 &#13;
            <option value="062">62</option>&#13;
		 &#13;
            <option value="063">63</option>&#13;
		 &#13;
            <option value="064">64</option>&#13;
		 &#13;
            <option value="065">65</option>&#13;
		 &#13;
            <option value="066">66</option>&#13;
		 &#13;
            <option value="067">67</option>&#13;
		 &#13;
            <option value="068">68</option>&#13;
		 &#13;
            <option value="069">69</option>&#13;
		 &#13;
            <option value="070">70</option>&#13;
		 &#13;
            <option value="071">71</option>&#13;
		 &#13;
            <option value="072">72</option>&#13;
		 &#13;
            <option value="073">73</option>&#13;
		 &#13;
            <option value="074">74</option>&#13;
		 &#13;
            <option value="075">75</option>&#13;
		 &#13;
            <option value="076">76</option>&#13;
		 &#13;
            <option value="077">77</option>&#13;
		 &#13;
            <option value="078">78</option>&#13;
		 &#13;
            <option value="079">79</option>&#13;
		 &#13;
            <option value="080">80</option>&#13;
		 &#13;
            <option value="081">81</option>&#13;
		 &#13;
            <option value="082">82</option>&#13;
		 &#13;
            <option value="083">83</option>&#13;
		 &#13;
            <option value="084">84</option>&#13;
		 &#13;
            <option value="085">85</option>&#13;
		 &#13;
            <option value="086">86</option>&#13;
		 &#13;
            <option value="087">87</option>&#13;
		 &#13;
            <option value="088">88</option>&#13;
		 &#13;
            <option value="089">89</option>&#13;
		 &#13;
            <option value="090">90</option>&#13;
		 &#13;
            <option selected="selected" value="091">91</option>&#13;
		 &#13;
            <option value="092">92</option>&#13;
		 &#13;
            <option value="093">93</option>&#13;
		 &#13;
            <option value="094">94</option>&#13;
		 &#13;
            <option value="095">95</option>&#13;
		 &#13;
            <option value="096">96</option>&#13;
		 &#13;
            <option value="097">97</option>&#13;
		 &#13;
            <option value="098">98</option>&#13;
		 &#13;
            <option value="099">99</option>&#13;
		 &#13;
            <option value="100">100</option>&#13;
		 &#13;
            <option value="101">101</option>&#13;
		 &#13;
            <option value="102">102</option>&#13;
		 &#13;
            <option value="103">103</option>&#13;
		 &#13;
            <option value="104">104</option>&#13;
		 &#13;
            <option value="105">105</option>&#13;
		 &#13;
            <option value="106">106</option>&#13;
		 &#13;
            <option value="107">107</option>&#13;
		 &#13;
            <option value="108">108</option>&#13;
		 &#13;
            <option value="109">109</option>&#13;
		 &#13;
        </select></td>&#13;
        <td>年</td>&#13;
        <td width="25%"><select name="birthMonth" class="id_nb1" id="select2">&#13;
            &#13;
		    <option value="01">1</option>&#13;
			&#13;
		    <option value="02">2</option>&#13;
			&#13;
		    <option value="03">3</option>&#13;
			&#13;
		    <option value="04">4</option>&#13;
			&#13;
		    <option selected="selected" value="05">5</option>&#13;
			&#13;
		    <option value="06">6</option>&#13;
			&#13;
		    <option value="07">7</option>&#13;
			&#13;
		    <option value="08">8</option>&#13;
			&#13;
		    <option value="09">9</option>&#13;
			&#13;
		    <option value="10">10</option>&#13;
			&#13;
		    <option value="11">11</option>&#13;
			&#13;
		    <option value="12">12</option>&#13;
			&#13;
        </select></td>&#13;
        <td>月</td>&#13;
        <td width="25%"><select name="birthDay" class="id_nb1" id="select3">&#13;
          &#13;
		  <option value="01">1</option>&#13;
		  &#13;
		  <option value="02">2</option>&#13;
		  &#13;
		  <option value="03">3</option>&#13;
		  &#13;
		  <option value="04">4</option>&#13;
		  &#13;
		  <option value="05">5</option>&#13;
		  &#13;
		  <option value="06">6</option>&#13;
		  &#13;
		  <option value="07">7</option>&#13;
		  &#13;
		  <option value="08">8</option>&#13;
		  &#13;
		  <option value="09">9</option>&#13;
		  &#13;
		  <option value="10">10</option>&#13;
		  &#13;
		  <option selected="selected" value="11">11</option>&#13;
		  &#13;
		  <option value="12">12</option>&#13;
		  &#13;
		  <option value="13">13</option>&#13;
		  &#13;
		  <option value="14">14</option>&#13;
		  &#13;
		  <option value="15">15</option>&#13;
		  &#13;
		  <option value="16">16</option>&#13;
		  &#13;
		  <option value="17">17</option>&#13;
		  &#13;
		  <option value="18">18</option>&#13;
		  &#13;
		  <option value="19">19</option>&#13;
		  &#13;
		  <option value="20">20</option>&#13;
		  &#13;
		  <option value="21">21</option>&#13;
		  &#13;
		  <option value="22">22</option>&#13;
		  &#13;
		  <option value="23">23</option>&#13;
		  &#13;
		  <option value="24">24</option>&#13;
		  &#13;
		  <option value="25">25</option>&#13;
		  &#13;
		  <option value="26">26</option>&#13;
		  &#13;
		  <option value="27">27</option>&#13;
		  &#13;
		  <option value="28">28</option>&#13;
		  &#13;
		  <option value="29">29</option>&#13;
		  &#13;
		  <option value="30">30</option>&#13;
		  &#13;
		  <option value="31">31</option>&#13;
		  &#13;
        </select></td>&#13;
        <td>日</td>&#13;
      </tr>&#13;
      </table></td>&#13;
  </tr>&#13;
  <tr>&#13;
    <td>驗證碼：</td>&#13;
  </tr>&#13;
  <tr>&#13;
    <td><table width="100%" border="0" cellspacing="0" cellpadding="0">&#13;
      <tr>&#13;
        <td width="22%" height="62" align="left" valign="bottom"><input name="validateCode" type="text" class="id_nb1" maxlength="4" autocomplete="off" /></td>&#13;
        <td width="45%" height="62" align="right" valign="bottom"><img src="/m3-emv-mobo/verifyCodeServlet" id="imgObj" width="215" height="61" /></td>&#13;
        <td width="30%" height="62" align="right" valign="bottom"><a href="javascript:void(0);" onclick="changeImg('imgObj','imgObj2')"><img src="/m3/images/mobo/bt03.png" width="148" height="62" /></a></td>&#13;
      </tr>&#13;
      </table></td>&#13;
  </tr>&#13;
  </table>&#13;
     <input type="hidden" name="queryType" value="0" />&#13;
      <input type="hidden" name="thisPage" value="1" />&#13;
     &#13;
</div>&#13;
  </form>&#13;
</div>&#13;
<!--按鈕-->&#13;
<div class="bt01"><a href="javascript:void(0);" onclick="moboQuerySubmit('personSubmit','0');"><img src="/m3/images/mobo/bt01.png" width="100%" /></a></div>&#13;
<div class="bt01"><a href="javascript:void(0);" onclick="moboQuerySubmit('personSubmit','1');"><img src="/m3/images/mobo/bt02.png" width="100%" /></a></div>&#13;
</div>&#13;
 <!-- 查詢表單:個人 End -->&#13;
 <!-- 查詢表單:法人 Start-->&#13;
 <div id="company" style="display: none">&#13;
<div class="irregularities_top">&#13;
&#13;
<table width="100%" border="0" cellspacing="0" cellpadding="0">&#13;
  <tr>&#13;
    <td valign="bottom" width="33%"><a href="javascript:void(0);" onclick="changeDisplay('company','person')"><img src="/m3/images/mobo/icon-06.png" width="100%" /></a></td>&#13;
    <td valign="bottom" width="33%"><img src="/m3/images/mobo/icon-05.png" width="100%" /></td>&#13;
    <td valign="bottom" width="34%"><img src="/m3/images/mobo/icon-04.png" width="101%" /></td>&#13;
  </tr>&#13;
  </table>&#13;
  <form action="moboTrafficFineResult" method="post" id="companySubmit">&#13;
  <div class="irregularities_main"><table width="95%" border="0" align="center" cellpadding="0" cellspacing="0">&#13;
  <tr>&#13;
    <td>統一編號：</td>&#13;
    </tr>&#13;
  <tr>&#13;
    <td><input name="searchID" type="text" class="id_nb1" id="textfield" maxlength="8" autocomplete="off" onkeydown="ValidateNumber(this,this.value);" onkeyup="ValidateNumber(this,this.value);" />&#13;
    </td>&#13;
    </tr>&#13;
  <tr>&#13;
    <td>驗證碼：</td>&#13;
  </tr>&#13;
  <tr>&#13;
    <td><table width="100%" border="0" cellspacing="0" cellpadding="0">&#13;
      <tr>&#13;
        <td width="22%" height="62" align="left" valign="bottom"><input name="validateCode" type="text" class="id_nb1" maxlength="4" autocomplete="off" /></td>&#13;
        <td width="45%" height="62" align="right" valign="bottom"><img src="/m3-emv-mobo/verifyCodeServlet" id="imgObj2" width="215" height="61" /></td>&#13;
        <td width="30%" height="62" align="right" valign="bottom"> <a href="javascript:void(0);" onclick="changeImg('imgObj','imgObj2')"><img src="/m3/images/mobo/bt03.png" width="148" height="62" /></a></td>&#13;
      </tr>&#13;
      </table></td>&#13;
    </tr>&#13;
   </table>&#13;
   </div>&#13;
   <input type="hidden" name="queryType" value="1" />&#13;
   <input type="hidden" name="thisPage" value="1" />&#13;
   &#13;
   &#13;
 </form>&#13;
</div>&#13;
&#13;
<!--按鈕-->&#13;
<div class="bt01"><a href="javascript:void(0);" onclick="moboQuerySubmit('companySubmit','0');"><img src="/m3/images/mobo/bt01.png" width="100%" /></a></div>&#13;
<div class="bt01"><a href="javascript:void(0);" onclick="moboQuerySubmit('companySubmit','1');"><img src="/m3/images/mobo/bt02.png" width="100%" /></a></div>&#13;
</div>&#13;
<!-- 查詢表單:法人 End -->&#13;
<!--注意事項-->&#13;
&#13;
<div class="link_text03" id="moboTitle">注意事項</div>&#13;
<div class="note" id="moboNotice">這裡可以打注意事項，這裡可以打注意事項，這裡可以打注意事項，這裡可以打注意事項，這裡可以打注意事項</div>&#13;
<!-- footer start -->&#13;
<div id="footer">地址：10863臺北市萬華區東園街65號<br />&#13;
總機：(02)2307-0123(代表號)  監理及大客車投訴專線：0800-231035<br />  系統操作服務專線0800-080-412(由網站建置廠商中華電信客服提供服務) <br />&#13;
  交通部公路總局 版權所有<br />&#13;
  如有監理業務疑問請向<a href="/m3-emv/news/office"><span class="link_text01">全國各監理機關</span></a>洽詢</div>&#13;
<!-- footer end -->&#13;
</body>&#13;
</html>'''

errorList = ['驗證碼不存在', '身分證號(或統一編號)格式不正確', '請重新查詢！']

# print(any(error in htmlTrue for error in errorList))
if any(error in html for error in errorList) == 'True':
    print(11111)
    pass
else:
    text = pq(htmlTrue)
    res = text('.irregularities_table01').text()
    a = res.splitlines()
    b = dict(zip())
    print(a)
    # print(res)

