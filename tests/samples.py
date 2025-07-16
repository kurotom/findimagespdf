# -*- coding: utf-8 -*-
"""
"""

correct_PDF_direct = b"""%PDF-1.4
1 0 obj
<<
  /Type /Catalog
  /Pages 2 0 R
>>
endobj
2 0 obj
<<
  /Type /Pages
  /Kids [3 0 R]
  /Count 1
>>
endobj
3 0 obj
<<
  /Type /Page
  /Parent 2 0 R
  /Resources << /XObject << /Im1 4 0 R >> >>
  /MediaBox [0 0 100 100]
  /Contents 5 0 R
>>
endobj
4 0 obj
<<
  /Type /XObject
  /Subtype /Image
  /Width 4
  /Height 4
  /ColorSpace /DeviceRGB
  /BitsPerComponent 8
  /Length 48
>>
stream
\xff\x00\x00\x00\xff\x00\x00\x00\xff\xff\xff\x00\xff\x00\xff\x00\xff\x00
\x00\xff\xff\x00\x00\xff\xff\x00\x00\xff\xff\xff\xff\x00\x00\x00\x00\x00
\xff\xff\x00\xff\x00\x00\xff\x00\x00\x00\xff\xff\x00\x00\xff\x00
endstream
endobj
5 0 obj
<< /Length 35 >>
stream
q
100 0 0 100 0 0 cm
/Im1 Do
Q
endstream
endobj
xref
0 6
0000000000 65535 f
0000000010 00000 n
0000000060 00000 n
0000000119 00000 n
0000000260 00000 n
0000000480 00000 n
trailer
<<
  /Size 6
  /Root 1 0 R
>>
startxref
600
%%EOF
"""

no_height_width_image = b"""%PDF-1.4
1 0 obj
<<
  /Type /Catalog
  /Pages 2 0 R
>>
endobj
2 0 obj
<<
  /Type /Pages
  /Kids [3 0 R]
  /Count 1
>>
endobj
3 0 obj
<<
  /Type /Page
  /Parent 2 0 R
  /Resources << /XObject << /Im1 4 0 R >> >>
  /MediaBox [0 0 100 100]
  /Contents 5 0 R
>>
endobj
4 0 obj
<<
  /Type /XObject
  /Subtype /Image
  /ColorSpace /DeviceRGB
  /BitsPerComponent 8
  /Length 24
>>
stream
\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff
endstream
endobj
5 0 obj
<< /Length 35 >>
stream
q
100 0 0 100 0 0 cm
/Im1 Do
Q
endstream
endobj
xref
0 6
0000000000 65535 f
0000000010 00000 n
0000000060 00000 n
0000000119 00000 n
0000000260 00000 n
0000000430 00000 n
trailer
<<
  /Size 6
  /Root 1 0 R
>>
startxref
550
%%EOF
"""

correct_PDF_indirect = b"""%PDF-1.4
1 0 obj
<< /Type /Catalog /Pages 2 0 R >>
endobj
2 0 obj
<< /Type /Pages /Kids [3 0 R] /Count 1 >>
endobj
3 0 obj
<< /Type /Page /Parent 2 0 R /Resources << /XObject << /Im1 4 0 R >> >> /MediaBox [0 0 200 200] /Contents 5 0 R >>
endobj
4 0 obj
<<
  /Type /XObject
  /Subtype /Image
  /ColorSpace /DeviceRGB
  /BitsPerComponent 8
  /Width 8 0 R
  /Height 9 0 R
  /Filter /DCTDecode
  /Length 50
>>
stream
\xff\xd8\xff\xe0JPEGDATAJPEGDATAJPEGDATAJPEGDATAJPEGDATA\xff\xd9
endstream
endobj
5 0 obj
<< /Length 35 >>
stream
q
200 0 0 200 0 0 cm
/Im1 Do
Q
endstream
endobj
8 0 obj
32
endobj
9 0 obj
32
endobj
xref
0 10
0000000000 65535 f
0000000010 00000 n
0000000073 00000 n
0000000136 00000 n
0000000274 00000 n
0000000530 00000 n
0000000000 00000 f
0000000000 00000 f
0000000600 00000 n
0000000616 00000 n
trailer
<< /Size 10 /Root 1 0 R >>
startxref
593
%%EOF
"""

no_height_image_indirect = b"""%PDF-1.4
1 0 obj
<< /Type /Catalog
   /Pages 2 0 R
>>
endobj
2 0 obj
<< /Type /Pages
   /Kids [3 0 R]
   /Count 1
>>
endobj
3 0 obj
<< /Type /Page
   /Parent 2 0 R
   /Resources <<
      /XObject << /Im1 5 0 R >>
   >>
   /Contents 4 0 R
   /MediaBox [0 0 100 100]
>>
endobj
4 0 obj
<< /Length 35 >>
stream
q
100 0 0 100 0 0 cm
/Im1 Do
Q
endstream
endobj
5 0 obj
<< /Type /XObject
   /Subtype /Image
   /Width 10 0 R
   /ColorSpace /DeviceRGB
   /BitsPerComponent 8
   /Length 6
   /Filter /ASCIIHexDecode
>>
stream
FF00FF>
endstream
endobj
10 0 obj
12
endobj
11 0 obj
18
endobj
xref
0 12
0000000000 65535 f
0000000010 00000 n
0000000074 00000 n
0000000129 00000 n
0000000254 00000 n
0000000316 00000 n
0000000000 65535 f
0000000000 65535 f
0000000000 65535 f
0000000000 65535 f
0000000465 00000 n
0000000480 00000 n
trailer
<< /Size 12
   /Root 1 0 R
>>
startxref
497
%%EOF
"""

pdf_invalid_ref_indirect = b"""%PDF-1.4
1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj
2 0 obj << /Type /Pages /Count 1 /Kids [3 0 R] >> endobj
3 0 obj << /Type /Page /Parent 2 0 R /Resources << /XObject << /Im1 4 0 R >> >> /Contents 5 0 R >> endobj
4 0 obj
<< /Type /XObject /Subtype /Image
   /Width 99 9 R
   /Height 11 0 R
   /ColorSpace /DeviceRGB /BitsPerComponent 8
   /Length 4 /Filter /ASCIIHexDecode >>
stream
FF>
endstream
endobj
5 0 obj << /Length 10 >> stream /Im1 Do endstream endobj
11 0 obj 888 endobj
xref
0 12
0000000000 65535 f
0000000010 00000 n
0000000051 00000 n
0000000102 00000 n
0000000222 00000 n
0000000410 00000 n
0000000000 65535 f
0000000000 65535 f
0000000000 65535 f
0000000000 65535 f
0000000000 65535 f
0000000490 00000 n
trailer
<< /Size 12 /Root 1 0 R >>
startxref
520
%%EOF
"""

pdf_mixed_images_indirect = b"""%PDF-1.4
1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj
2 0 obj << /Type /Pages /Kids [3 0 R] /Count 1 >> endobj
3 0 obj << /Type /Page /Parent 2 0 R
  /Resources << /XObject <<
    /Im1 4 0 R
    /Im2 5 0 R
    /Im3 6 0 R
  >> >>
  /Contents 7 0 R
>> endobj
4 0 obj
<< /Type /XObject /Subtype /Image
   /Width 10 0 R
   /Height 11 0 R
   /ColorSpace /DeviceRGB /BitsPerComponent 8
   /Length 4 /Filter /ASCIIHexDecode >>
stream
A1B>
endstream
endobj
5 0 obj
<< /Type /XObject /Subtype /Image
   /Width 12 0 R
   /Height 12 0 R
   /ColorSpace /DeviceRGB /BitsPerComponent 8
   /Length 4 /Filter /ASCIIHexDecode >>
stream
C2D>
endstream
endobj
6 0 obj
<< /Type /XObject /Subtype /Image
   /Width 12 0 R
   /Height 99 9 R
   /ColorSpace /DeviceRGB /BitsPerComponent 8
   /Length 4 /Filter /ASCIIHexDecode >>
stream
EEE>
endstream
endobj
7 0 obj << /Length 20 >> stream
/Im1 Do /Im2 Do /Im3 Do
endstream
endobj
10 0 obj 100 endobj
11 0 obj 200 endobj
12 0 obj
 300
endobj
xref
0 13
0000000000 65535 f
0000000010 00000 n
0000000060 00000 n
0000000123 00000 n
0000000300 00000 n
0000000490 00000 n
0000000678 00000 n
0000000868 00000 n
0000000000 65535 f
0000000000 65535 f
0000000958 00000 n
0000000975 00000 n
0000000992 00000 n
trailer
<< /Size 13 /Root 1 0 R >>
startxref
1015
%%EOF
"""
