<?php if ($_POST["pass"]!="123") {
	die ('wrong password.');
} ?>
<!DOCTYPE HTML>
<html>
<head>
    <title>HTML5 Drag and drop</title>
    <style>
		#section{font-family: "Georgia";}
        .container{display:inline-block;min-height:200px;min-width:360px;color:#f30;padding:30px;border:3px solid #ddd;-moz-border-radius:10px;-webkit-border-radius:10px;border-radius:10px;}
		.preview{max-width:360px;}
		#files-list{position:absolute;top:0;left:500px;}
		#list{width:460px;}
		#list .preview{max-width:250px;}
		#list p{color:#888;font-size:12px;}
		#list .green{color:#09c;}
    </style>
</head>
<body>

    <div id="section">
        <p>Drop files here:</p>
        <div id="container" class="container">
            
        </div>
		<div id ="files-list">
			<p>History:</p>
			<ul id="list"></ul>
		</div>
    </div>

	<script>
	
	if (window.FileReader) {

		var list = document.getElementById('list'),
			cnt = document.getElementById('container');

		// �ж��Ƿ�ͼƬ
		function isImage(type) {
			switch (type) {
			case 'image/jpeg':
			case 'image/png':
			case 'image/gif':
			case 'image/bmp':
			case 'image/jpg':
				return true;
			default:
				return false;
			}
		}

		// �����Ϸ��ļ��б�
		function handleFileSelect(evt) {
			evt.stopPropagation();
			evt.preventDefault();

			var files = evt.dataTransfer.files;

			for (var i = 0, f; f = files[i]; i++) {

				var t = f.type ? f.type : 'n/a',
					reader = new FileReader(),
					looks = function (f, img) {
						list.innerHTML += '<li><strong>' + f.name + '</strong> (' + t +
							') - ' + f.size + ' bytes<p>' + img + '</p></li>';
						cnt.innerHTML = img;
					},
					isImg = isImage(t),
					img;

				// ����õ���ͼƬ
				if (isImg) {
					reader.onload = (function (theFile) {
						return function (e) {
							img = '<img class="preview" src="' + e.target.result + '" title="' + theFile.name + '"/>';
							looks(theFile, img);
						};
					})(f)
					reader.readAsDataURL(f);
				} else {
					img = 'Not an image file.';
					looks(f, img);
				}

			}

		}
		
		// ��������ϳ�Ч��
		function handleDragEnter(evt){ this.setAttribute('style', 'border-style:dashed;'); }
		function handleDragLeave(evt){ this.setAttribute('style', ''); }

		// �����ļ������¼�����ֹ�����Ĭ���¼��������ض���
		function handleDragOver(evt) {
			evt.stopPropagation();
			evt.preventDefault();
		}
		
		cnt.addEventListener('dragenter', handleDragEnter, false);
		cnt.addEventListener('dragover', handleDragOver, false);
		cnt.addEventListener('drop', handleFileSelect, false);
		cnt.addEventListener('dragleave', handleDragLeave, false);
		
	} else {
		document.getElementById('section').innerHTML = '����������֧�ְ���ͬѧ';
	}
	
	</script>
    
</body>
</html>
