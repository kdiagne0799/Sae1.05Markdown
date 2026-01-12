# 🛡️ Global Network Security Report

## 1. Critical Threat: Targeted SSH Attack
- 🔴 **Main Assault**: `192.168.190.130` (66 packets). Brute Force confirmed.

## 2. Other Detected Anomalies
- ⚠️ **Port Scanning**: Host probed **135** different ports.
- ⚠️ **ICMP Flood**: 84 packets detected. Potential DoS.

## 3. Traffic Sample (Top 30)
| Timestamp | Source IP | Src Port | Dest IP | Dest Port | Flags | Length | Info |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 15:34:04.766656 | BP-Linux8 | ssh | 192.168.190.130 | 50019 | `P.` | 108 | Flags [P.], seq 2243505564:224... |
| 15:34:04.766694 | BP-Linux8 | ssh | 192.168.190.130 | 50019 | `P.` | 36 | Flags [P.], seq 108:144, ack 1... |
| 15:34:04.766723 | BP-Linux8 | ssh | 192.168.190.130 | 50019 | `P.` | 108 | Flags [P.], seq 144:252, ack 1... |
| 15:34:04.766744 | BP-Linux8 | ssh | 192.168.190.130 | 50019 | `P.` | 36 | Flags [P.], seq 252:288, ack 1... |
| 15:34:04.785366 | 192.168.190.130 | 50019 | BP-Linux8 | ssh | `.` | 0 | Flags [.], ack 108, win 7319, ... |
| 15:34:04.785384 | 192.168.190.130 | 50019 | BP-Linux8 | ssh | `.` | 0 | Flags [.], ack 144, win 7318, ... |
| 15:34:04.785406 | 192.168.190.130 | 50019 | BP-Linux8 | ssh | `.` | 0 | Flags [.], ack 252, win 7316, ... |
| 15:34:04.785454 | 192.168.190.130 | 50019 | BP-Linux8 | ssh | `.` | 0 | Flags [.], ack 288, win 7320, ... |
| 15:34:05.768334 | BP-Linux8 | 58466 | ns1.lan.rt | domain | `None` | 0 | 16550+ PTR? 130.190.168.192.in... |
| 15:34:05.769075 | ns1.lan.rt | domain | BP-Linux8 | 58466 | `None` | 0 | 16550 NXDomain 0/1/0 (112)... |
| 15:34:06.669393 | 192.168.190.130 | 50245 | BP-Linux8 | ssh | `P.` | 36 | Flags [P.], seq 1601828178:160... |
| 15:34:06.669906 | BP-Linux8 | ssh | 192.168.190.130 | 50245 | `P.` | 36 | Flags [P.], seq 1:37, ack 36, ... |
| 15:34:06.679262 | BP-Linux8 | 53220 | ns1.lan.rt | domain | `None` | 0 | 54801+ A? lacampora.org. (31)... |
| 15:34:06.679971 | ns1.lan.rt | domain | BP-Linux8 | 53220 | `None` | 0 | 54801 1/0/0 A 184.107.43.74 (4... |
| 15:34:06.681188 | BP-Linux8 | ssh | 192.168.190.130 | 50245 | `P.` | 116 | Flags [P.], seq 37:153, ack 36... |
| 15:34:06.681222 | BP-Linux8 | ssh | 192.168.190.130 | 50245 | `P.` | 36 | Flags [P.], seq 153:189, ack 3... |
| 15:34:06.681248 | 190-0-175-100.gba.solunet.com.ar | 2465 | 184.107.43.74 | http | `S` | 120 | Flags [S], seq 326991629:32699... |
| 15:34:06.681274 | 190-0-175-100.gba.solunet.com.ar | 2466 | 184.107.43.74 | http | `S` | 120 | Flags [S], seq 920517760:92051... |
| 15:34:06.681294 | 190-0-175-100.gba.solunet.com.ar | 2467 | 184.107.43.74 | http | `S` | 120 | Flags [S], seq 556803824:55680... |
| 15:34:06.681312 | 190-0-175-100.gba.solunet.com.ar | 2468 | 184.107.43.74 | http | `S` | 120 | Flags [S], seq 1921632185:1921... |
| 15:34:06.681328 | 190-0-175-100.gba.solunet.com.ar | 2469 | 184.107.43.74 | http | `S` | 120 | Flags [S], seq 1170972654:1170... |
| 15:34:06.681345 | 190-0-175-100.gba.solunet.com.ar | 2470 | 184.107.43.74 | http | `S` | 120 | Flags [S], seq 754504426:75450... |
| 15:34:06.681362 | 190-0-175-100.gba.solunet.com.ar | 2471 | 184.107.43.74 | http | `S` | 120 | Flags [S], seq 669863147:66986... |
| 15:34:06.681379 | 190-0-175-100.gba.solunet.com.ar | 2472 | 184.107.43.74 | http | `S` | 120 | Flags [S], seq 1036593434:1036... |
| 15:34:06.681396 | 190-0-175-100.gba.solunet.com.ar | 2473 | 184.107.43.74 | http | `S` | 120 | Flags [S], seq 473640609:47364... |
| 15:34:06.681413 | 190-0-175-100.gba.solunet.com.ar | 2474 | 184.107.43.74 | http | `S` | 120 | Flags [S], seq 294639309:29463... |
| 15:34:06.681430 | 190-0-175-100.gba.solunet.com.ar | 2475 | 184.107.43.74 | http | `S` | 120 | Flags [S], seq 2003734750:2003... |
| 15:34:06.681446 | 190-0-175-100.gba.solunet.com.ar | 2476 | 184.107.43.74 | http | `S` | 120 | Flags [S], seq 943277646:94327... |
| 15:34:06.681463 | 190-0-175-100.gba.solunet.com.ar | 2477 | 184.107.43.74 | http | `S` | 120 | Flags [S], seq 612921749:61292... |
| 15:34:06.681480 | 190-0-175-100.gba.solunet.com.ar | 2478 | 184.107.43.74 | http | `S` | 120 | Flags [S], seq 1079269685:1079... |
