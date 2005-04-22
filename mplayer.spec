#
# Conditional build:
%bcond_with	directfb	# with DirectFB video output
%bcond_with	divx4linux	# with divx4linux a/v support (binaries, instead
				#  of included OpenDivx)

%bcond_with	dxr3		# enable use of DXR3/H+ hardware MPEG decoder
%bcond_with	ggi		# with ggi video output
%bcond_with	live		# enable use of live.com libraries
%bcond_with	nas		# with NAS audio output
%bcond_with	svga		# with svgalib video output
%bcond_with	osd		# with osd menu support

%bcond_with	altivec		# with altivec support (won't run w/o altivec
				# due to instruction used in CPU detection(?))

%bcond_with	xmms		# with XMMS inputplugin support

%bcond_without	aalib		# without aalib video output
%bcond_without	jack		# without JACKD support
%bcond_without	alsa		# without ALSA audio output
%bcond_without	arts		# without arts audio output
%bcond_without	caca		# without libcaca video output
%bcond_without	dshow		# disable DirectShow support
%bcond_without	gui		# without GTK+ GUI
%bcond_without	joystick	# disable joystick support
%bcond_without	libdv		# disable libdv en/decoding support
%bcond_without	lirc		# without lirc support
%bcond_without	mad		# without mad (audio MPEG) support
%bcond_without	polyp		# without polyp audio output
%bcond_without	quicktime	# without binary quicktime dll support
%bcond_without	real		# without Real* 8/9 codecs support
%bcond_without	runtime		# disable runtime cpu detection, just detect CPU
				#  in compile time (advertised by mplayer
				#  authors as working faster); in this case
				#  mplayer may not work on machine other then
				#  where it was compiled
%bcond_without	select		# disable audio select() support (for example
				# required this option ALSA or Vortex2 driver)
%bcond_without	smb		# disable Samba (SMB) input support
%bcond_without	theora		# without theora support
%bcond_without	win32		# without win32 codecs support
%bcond_without	vorbis		# without Ogg-Vorbis audio support
%bcond_without	mencoder	# disable mencoder (a/v encoder) compilation
%bcond_without	libdts		# disable libdts support

%bcond_with	gtk2		# EXPERIMENTAL support for GTK+ version 2
%bcond_with	xlibs

%ifnarch %{ix86}
%undefine	with_win32
%undefine	with_quicktime
%endif

# set it to 0, or 1
%define		snapshot	0

%define		sname		MPlayer
%define		snap		%{nil}

%define		pre		pre7

Summary:	Yet another movie player
Summary(es):	Otro reproductor de películas
Summary(ko):	¸®´ª½º¿ë ¹Ìµð¾îÇÃ·¹ÀÌ¾î
Summary(pl):	Jeszcze jeden odtwarzacz filmów
Summary(pt_BR):	Reprodutor de filmes
Name:		mplayer
Version:	1.0
Release:	1.%{pre}.1
Epoch:		2
License:	GPL
Group:		X11/Applications/Multimedia
%if %{snapshot}
#Source0:	ftp://ftp1.mplayerhq.hu/%{sname}/cvs/%{sname}-%{snap}.tar.bz2
#Source0:	%{name}-%{snap}.tar.bz2
#Source1:	libavcodec-%{snap}.tar.bz2
%else
Source0:	ftp://ftp1.mplayerhq.hu/%{sname}/releases/%{sname}-%{version}%{pre}.tar.bz2
# Source0-md5:	5fadd6957d3aab989cd760ff38fb8fdf
%endif
Source3:	ftp://ftp1.mplayerhq.hu/%{sname}/releases/fonts/font-arial-iso-8859-2.tar.bz2
# Source3-md5:	7b47904a925cf58ea546ca15f3df160c
Source4:	ftp://ftp1.mplayerhq.hu/%{sname}/Skin/Blue-1.4.tar.bz2
# Source4-md5:	05dd8e4f11a715c9e5d2abf1cdeb907c
Source5:	g%{name}.desktop
Source6:	ftp://ftp1.mplayerhq.hu/%{sname}/releases/fonts/font-arial-iso-8859-1.tar.bz2
# Source6-md5:	1ecd31d17b51f16332b1fcc7da36b312
Source7:	%{name}.png
Patch0:		%{name}-no_libnsl.patch
Patch1:		%{name}-cp1250-fontdesc.patch
Patch2:		%{name}-codec.patch
Patch3:		%{name}-home_etc.patch
Patch4:		%{name}-350.patch
Patch5:		%{name}-configure.patch
Patch6:		%{name}-gtk+2.patch
Patch7:		%{name}-alpha.patch
Patch8:		%{name}-altivec.patch
Patch9:		%{name}-assembly.patch
Patch10:	%{name}-pcmsplit.patch
Patch11:	%{name}-bio2jack.patch
URL:		http://www.mplayerhq.hu/
%{?with_directfb:BuildRequires:	DirectFB-devel}
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.1.7
%if %{with xlibs}
BuildRequires:	libXv-devel
%else
BuildRequires:	XFree86-devel >= 4.0.2
%endif
%{?with_aalib:BuildRequires:	aalib-devel}
%{?with_alsa:BuildRequires:	alsa-lib-devel}
%{?with_arts:BuildRequires:	artsc-devel}
BuildRequires:	audiofile-devel
BuildRequires:	cdparanoia-III-devel
%{?with_divx4linux:BuildRequires:	divx4linux-devel >= 1:5.01.20020418}
%{?with_dxr3:BuildRequires:	em8300-devel}
BuildRequires:	enca-devel
BuildRequires:	esound-devel
BuildRequires:	faad2-devel >= 2.0
BuildRequires:	freetype-devel
%ifarch ppc
%{?with_altivec:BuildRequires:	gcc >= 5:3.3.2-3}
%endif
%if %{with gui}
BuildRequires:	gtk+%{?with_gtk2:2}-devel
%endif
BuildRequires:	lame-libs-devel
%{?with_jack:BuildRequires:	libbio2jack-devel}
%{?with_caca:BuildRequires:	libcaca-devel}
%{?with_libdts:BuildRequires:	libdts-devel}
%{?with_libdv:BuildRequires:	libdv-devel}
%{?with_ggi:BuildRequires:	libggi-devel}
BuildRequires:	libjpeg-devel
%{?with_mad:BuildRequires:	libmad-devel}
BuildRequires:	libpng-devel
%{?with_smb:BuildRequires:	libsmbclient-devel}
%{?with_dshow:BuildRequires:	libstdc++-devel}
%{?with_theora:BuildRequires:	libtheora-devel}
%{?with_vorbis:BuildRequires:	libvorbis-devel}
BuildRequires:	libungif-devel
BuildRequires:	libxslt-progs
%{?with_lirc:BuildRequires:	lirc-devel}
%{?with_live:BuildRequires:	live}
BuildRequires:	lzo-devel
%{?with_nas:BuildRequires:	nas-devel}
BuildRequires:	ncurses-devel
%{?with_polyp:BuildRequires:	polypaudio-devel}
%{?with_svga:BuildRequires:	svgalib-devel}
%{?with_xmms:BuildRequires:	xmms-libs}
BuildRequires:	xvid-devel >= 1:0.9.0
BuildRequires:	zlib-devel
Requires(post,postun):	/sbin/ldconfig
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		specflags	-fomit-frame-pointer
%define		specflags_alpha	-mmax
%if %{with altivec}
%define		specflags_ppc	-maltivec -mabi=altivec
%endif

%description
Movie player. Supported input formats: VCD (VideoCD), MPEG1/2, RIFF
AVI, ASF 1.0, Quicktime. Supported audio codecs: PCM (uncompressed),
MPEG layer 2/3, AC3, aLaw, MS-GSM, Win32 ACM. Supported video codecs:
MPEG 1 and MPEG 2, Win32 ICM (VfW), OpenDivX. Supported output
devices: Matrox G200/G400 hardware, Matrox G200/G400 overlay, X11
optionally with SHM extension, X11 using overlays with the Xvideo
extension, OpenGL renderer, Matrox G400 YUV support on framebuffer
Voodoo2/3 hardware, SDL v1.1.7 driver etc.

If you want to use win32 codecs install w32codec package.

%description -l es
Reproductor video. Formatos de entrada soportados: VCD (VideoCD),
MPEG1/2, RIFF AVI, ASF 1.0, Quicktime. Codecs de audio soportados: PCM
(uncompressed), MPEG layer 2/3, AC3, aLaw, MS-GSM, Win32 ACM. Codecs
de video soportados: MPEG 1 and MPEG 2, Win32 ICM (VfW), OpenDivX.
Dispositivos de salida soportados: Matrox G200/G400 hardware, Matrox
G200/G400 overlay, X11 optionalmente con la extensión SHM, X11 usando
overlays con la extensión Xvideo, plasmador OpenGL, soporte de Matrox
G400 YUV en hardware de framebuffer de Voodoo2/3, controlador SDL
v1.1.7 etc.

Si quiere usar codecs Win32, instale el paquete w32codec.

%description -l ko
MPlayer´Â ¸®´ª½º¿ë ¹«ºñÇÃ·¹ÀÌ¾îÀÔ´Ï´Ù. ´ëºÎºÐÀÇ mpeg, avi ±×¸®°í asf
ÆÄÀÏÀ» Àç»ýÇÕ´Ï´Ù. VCD, DVD, ½É Áö¾î DivX±îÁö º¼ ¼ö ÀÖ½À´Ï´Ù.
MPlayerÀÇ ¶Ç ´Ù¸¥ Å« Æ¯Â¡Àº Ãâ·Â µå¶óÀÌ¹ö°¡ ´Ù¾çÇÏ´Ù´Â °ÍÀÔ´Ï´Ù. X11,
Xv, DGA, OpenGL, SVGAlib, fbdev¿Í ÀÛµ¿ÇÏ¸ç, SDLÀÌ³ª
(Matrox/3dfx/SisµîÀÇ) Æ¯Á¤ Ä«µå¿¡ Á¾¼ÓµÈ ·Î¿ì·¹ º§ µå¶óÀÌ¹öµéµµ »ç¿ëÇÒ
¼ö ÀÖ½À´Ï´Ù. ´ëºÎºÐÀÇ Ãâ·Â µå¶óÀÌ¹öµéÀº ¼ÒÇÁÆ®¿þ¾î È¤Àº ÇÏµå¿þ¾îÀûÀÎ
Å©±âÁ¶Àý (scaling)À» Áö¿øÇÏ¹Ç·Î, ÀüÃ¼È­¸éÀ¸·Î ¿µ»óÀ» °¨»óÇÒ ¼ö
ÀÖ½À´Ï´Ù. »Ó¸¸¾Æ´Ï¶ó, ÇÑ±¹¾î, ¿µ¾î, Çë°¡¸®¾î, Ã¼ÄÚ¾î, ·¯½Ã¾Æ¾îµîÀÇ
ºÎµå·¯¿î(antialiased) ÀÚ¸·ÆùÆ®µµ »ç¿ëÇÒ ¼ö ÀÖ½À´Ï´Ù.

%description -l pl
Odtwarzacz wideo. Wspierane formaty wej¶ciowe: VCD (VideoCD), MPEG1/2,
RIFF AVI, ASF 1.0, Quicktime. Wspierane kodeki audio: PCM
(nieskompresowane), MPEG layer 2/3, AC3, aLaw, MS-GSM, Win32 ACM.
Wspierane kodeki wideo: MPEG 1 and MPEG 2, Win32 ICM (VfW), OpenDivX.
Wspierane urz±dzenia wyj¶ciowe: Matrox G200/G400, X11 opcjonalnie z
rozszerzeniem SHM, X11 z rozszerzeniem Xvideo, renderer OpenGL, Matrox
G400 u¿ywaj±c framebuffera, Voodoo2/3, SDL v1.1.7 itp.

Je¶li chcesz u¿ywaæ kodeków win32, zainstaluj pakiet w32codec.

%description -l pt_BR
MPlayer é um reprodutor de filmes que suporta vários codecs de vídeo e
áudio. Diferentes mecanismos de reprodução podem também ser
escolhidos, incluindo SDL, SVGALib, frame buffer, aalib, X11 e outros.

%prep
%if %{snapshot}
%setup -q -n %{name}-%{snap} -a 1 -a 3 -a 6
%else
%setup -q -n %{sname}-%{version}%{pre} -a 3 -a 6
%endif

cp -f etc/codecs.conf etc/codecs.win32.conf
%patch0 -p1
%patch1 -p0
##%patch2 -p1
##%patch3 -p1	-- old home_etc behavior
%patch4 -p1
%patch5 -p1
%if %{with gtk2}
%patch6 -p1
%endif
%patch7 -p1
%patch8 -p1
%patch9 -p1
#%%patch10 -p1
%patch11 -p1

# kill evil file, hackery not needed with llh
echo > osdep/kerneltwosix.h

find . -type d -name CVS -print | xargs rm -rf

%build
CFLAGS="%{rpmcflags}"
CC="%{__cc}"
export CC CFLAGS
./configure \
	--prefix=%{_prefix} \
	--confdir=%{_sysconfdir}/mplayer \
	--with-x11incdir=%{_prefix}/X11R6/include \
	--with-extraincdir=%{_includedir}/xvid \
%ifnarch %{ix86}
	--disable-mmx \
	--disable-mmx2 \
	--disable-3dnow \
	--disable-3dnowex \
	--disable-sse \
	--disable-sse2 \
	--disable-fastmemcpy \
%endif
%ifarch ppc
%{!?with_altivec:--disable-altivec} \
%endif
%{!?with_directfb:--disable-directfb} \
%{!?with_divx4linux:--disable-divx4linux} \
%{?with_divx4linux:--with-extraincdir=/usr/include/divx} \
%{!?with_dxr3:--disable-dxr3} \
%{!?with_ggi:--disable-ggi} \
%{?with_live:--enable-live --with-livelibdir=/usr/lib/liveMedia --with-extraincdir=/usr/include/liveMedia } \
%{!?with_live:--disable-live} \
%{!?with_nas:--disable-nas} \
%{!?with_svga:--disable-svga} \
%{!?with_aalib:--disable-aa} \
%{!?with_jack:--disable-jack} \
%{!?with_alsa:--disable-alsa} \
%{?with_alsa:--enable-alsa --disable-select} \
%{!?with_arts:--disable-arts} \
%{!?with_caca:--disable-caca} \
%{!?with_dshow:--disable-dshow} \
%{?with_gui:--enable-gui} \
%{?with_joystick:--enable-joystick} \
%{!?with_libdv:--disable-libdv} \
%{!?with_libdts:--disable-libdts} \
%{!?with_lirc:--disable-lirc} \
%{!?with_mad:--disable-mad} \
%{!?with_polyp:--disable-polyp} \
%{!?with_quicktime:--disable-qtx} \
%{!?with_real:--disable-real} \
%{!?with_runtime:--disable-runtime-cpudetection} \
%{?with_runtime:--enable-runtime-cpudetection} \
%{!?with_select:--disable-select} \
%{!?with_smb:--disable-smb} \
%{!?with_win32:--disable-win32} \
%{!?with_vorbis:--disable-vorbis} \
%{?with_osd:--enable-menu} \
%{!?with_theora:--disable-theora} \
%{?with_xmms:--enable-xmms --with-xmmsplugindir=%{_libdir}/xmms/Input --with-xmmslibdir=%{_libdir}} \
%{!?with_mencoder:--disable-mencoder} \
	--enable-external-faad \
	--enable-dga \
	--enable-fbdev \
	--enable-gl \
	--enable-mga \
	--enable-sdl \
	--enable-tdfxfb \
	--enable-vm \
	--enable-x11 \
	--enable-xmga \
	--enable-xv \
	--enable-xvmc \
	--enable-xvid \
	--enable-largefiles \
	--language=all \
	--with-codecsdir=%{_libdir}/codecs \
	--enable-dynamic-plugins

%{__make}

%{__make} -C DOCS/xml

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_sysconfdir}/mplayer} \
	$RPM_BUILD_ROOT%{_mandir}/{cs,de,es,fr,hu,it,pl,sv,zh_CN,}/man1 \
	$RPM_BUILD_ROOT{%{_datadir}/mplayer/Skin,%{_libdir}/mplayer/vidix} \
	$RPM_BUILD_ROOT%{_desktopdir}

# default config files
awk '/Delete this default/{a++};{if(!a){print}}' etc/example.conf > etc/mplayer.conf
install etc/{codecs,mplayer%{?with_osd:,menu},input}.conf $RPM_BUILD_ROOT%{_sysconfdir}/mplayer

# executables
%if %{with mencoder}
install mencoder $RPM_BUILD_ROOT%{_bindir}
%endif
install mplayer $RPM_BUILD_ROOT%{_bindir}
ln -sf mplayer $RPM_BUILD_ROOT%{_bindir}/gmplayer

# fonts
rm -f font-*/runme
cp -r font-* $RPM_BUILD_ROOT%{_datadir}/mplayer
ln -sf font-arial-iso-8859-2/font-arial-24-iso-8859-2 $RPM_BUILD_ROOT%{_datadir}/mplayer/font

# skin
bzip2 -dc %{SOURCE4} | tar xf - -C $RPM_BUILD_ROOT%{_datadir}/mplayer/Skin
rm -rf $RPM_BUILD_ROOT%{_datadir}/mplayer/Skin/*/CVS

# libraries
%ifarch %{ix86}
install libdha/libdha.so.1.0 $RPM_BUILD_ROOT%{_libdir}
install vidix/drivers/*.so $RPM_BUILD_ROOT%{_libdir}/mplayer/vidix
%endif

# X-files
install %{SOURCE5} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE7} $RPM_BUILD_ROOT%{_pixmapsdir}

# man pages
install DOCS/man/cs/*.1 $RPM_BUILD_ROOT%{_mandir}/cs/man1
install DOCS/man/de/*.1 $RPM_BUILD_ROOT%{_mandir}/de/man1
install DOCS/man/en/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install DOCS/man/es/*.1 $RPM_BUILD_ROOT%{_mandir}/es/man1
install DOCS/man/fr/*.1 $RPM_BUILD_ROOT%{_mandir}/fr/man1
install DOCS/man/hu/*.1 $RPM_BUILD_ROOT%{_mandir}/hu/man1
install DOCS/man/it/*.1 $RPM_BUILD_ROOT%{_mandir}/it/man1
install DOCS/man/pl/*.1 $RPM_BUILD_ROOT%{_mandir}/pl/man1
install DOCS/man/sv/*.1 $RPM_BUILD_ROOT%{_mandir}/sv/man1
install DOCS/man/zh/*.1 $RPM_BUILD_ROOT%{_mandir}/zh_CN/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
/sbin/ldconfig
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
umask 022
/sbin/ldconfig
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc DOCS/HTML/en/*.html DOCS/tech %{?with_win32:etc/codecs.win32.conf}
%lang(de) %doc DOCS/de
%lang(es) %doc DOCS/HTML/es
%lang(fr) %doc DOCS/HTML/fr
%lang(hu) %doc DOCS/HTML/hu
%lang(it) %doc DOCS/it
%lang(pl) %doc DOCS/HTML/pl
%lang(ru) %doc DOCS/HTML/ru
%lang(zh_CN) %doc DOCS/zh
%doc README AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%ifarch %{ix86}
%attr(755,root,root) %{_libdir}/libdha.so.*.*
%attr(755,root,root) %{_libdir}/mplayer
%endif
%{_datadir}/mplayer
%dir %{_sysconfdir}/mplayer
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/mplayer/*.conf
%{_mandir}/man1/*
%lang(cs) %{_mandir}/cs/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%lang(sv) %{_mandir}/sv/man1/*
%lang(zh_CN) %{_mandir}/zh_CN/man1/*
%if %{with gui}
%{_desktopdir}/*
%{_pixmapsdir}/*
%endif
