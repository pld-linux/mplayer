#
# Conditional build:
%bcond_with	directfb	# with DirectFB video output
%bcond_with	dxr3		# enable use of DXR3/H+ hardware MPEG decoder
%bcond_with	ggi		# with ggi video output
%bcond_with	nas		# with NAS audio output
%bcond_with	svga		# with svgalib video output
%bcond_without	osd		# with osd menu support
%bcond_without	altivec		# without altivec support
%bcond_without	x264		# without x264 support
%bcond_with	xmms		# with XMMS inputplugin support
%bcond_without	aalib		# without aalib video output
%bcond_without	jack		# without JACKD support
%bcond_without	alsa		# without ALSA audio output
%bcond_without	arts		# without arts audio output
%bcond_without	caca		# without libcaca video output
%bcond_without	cdparanoia	# without cdparanoia support
%bcond_without	dvdnav		# without dvdnav support
%bcond_without	enca		# disable using ENCA charset oracle library
%bcond_without	esd		# disable EsounD sound support
%bcond_without	faad		# disable FAAD2 (AAC) support
%bcond_without	gif		# disable GIF support
%bcond_without	gui		# without GTK+ GUI
%bcond_without	joystick	# disable joystick support
%bcond_without	libdts		# disable libdts support
%bcond_without	libdv		# disable libdv en/decoding support
%bcond_without	lirc		# without lirc support
%bcond_without	live		# without LIVE555 libraries
%bcond_without	lzo		# with LZO support (requires lzo 2.x)
%bcond_without	mad		# without mad (audio MPEG) support
%bcond_without	pulseaudio	# without pulseaudio output
%bcond_without	quicktime	# without binary quicktime dll support
%bcond_without	real		# without Real* 8/9 codecs support
%bcond_without	runtime		# disable runtime cpu detection, just detect CPU
				#  in compile time (advertised by mplayer authors as working faster); in this case
				#  mplayer may not work on machine other then where it was compiled
%bcond_without	select		# disable audio select() support (for example required this option ALSA or Vortex2 driver)
%bcond_without	smb		# disable Samba (SMB) input support
%bcond_without	theora		# without theora support
%bcond_without	win32		# without win32 codecs support
%bcond_without	vdpau		# disable vdpau
%bcond_without	vidix		# disable vidix
%bcond_without	vorbis		# without Ogg-Vorbis audio support
%bcond_with	system_vorbis	# use system libvorbis instead of internal tremor
%bcond_without	xvid		# disable XviD codec
%bcond_without	mencoder	# disable mencoder (a/v encoder) compilation
%bcond_without	sdl		# disable SDL
%bcond_without	doc		# don't build docs (slow)
%bcond_with	shared		# experimental libmplayer.so support
%bcond_without	amr		# enable Adaptive Multi Rate (AMR) speech codec support
%bcond_without	gnomess		# disable controling gnome screensaver
%bcond_without	ssse3		# sse3 optimizations (needs binutils >= 2.16.92)
%bcond_with	system_ffmpeg	# use ffmpeg-devel, rather bundled sources (likely needs ffmpeg from same svn revision than mplayer)
%bcond_with	on2		# with patches from On2 Flix Engine for Linux

%if %{with alsa}
%undefine	with_select
%endif

%if %{without vorbis}
%undefine	with_system_vorbis
%endif

%ifnarch %{ix86}
%undefine	with_win32
%undefine	with_quicktime
%undefine	with_vidix
%endif

%ifnarch %{ix86} %{x8664} ppc ppc64
%undefine	with_runtime
%endif

%if %{_lib} == "lib64"
%define		_suf	64
%else
%define		_suf	32
%endif

%define		subver	rc4
%define		svnver	29930
%define		rel	4

Summary:	MPlayer - THE Movie Player for UN*X
Summary(de.UTF-8):	MPlayer ist ein unter der freien GPL-Lizenz stehender Media-Player
Summary(es.UTF-8):	Otro reproductor de películas
Summary(ko.UTF-8):	리눅스용 미디어플레이어
Summary(pl.UTF-8):	Odtwarzacz filmów dla systemów uniksowych
Summary(pt_BR.UTF-8):	Reprodutor de filmes
Name:		mplayer
Version:	1.0
Release:	5.%{subver}_svn%{svnver}.%{rel}
# DO NOT increase epoch unless it's really neccessary!
# especially such changes like pre7->pre7try2, increase Release instead!
# PS: $ rpmvercmp pre7try2 pre7
# pre7try2 > pre7
Epoch:		3
License:	GPL
Group:		Applications/Multimedia
Source0:	mplayer-r%{svnver}.tar.xz
# Source0-md5:	b3261cc2e8cb2240131e58e0ce734f8a
Source3:	ftp://ftp1.mplayerhq.hu/MPlayer/releases/fonts/font-arial-iso-8859-2.tar.bz2
# Source3-md5:	7b47904a925cf58ea546ca15f3df160c
Source5:	g%{name}.desktop
Source6:	ftp://ftp2.mplayerhq.hu/MPlayer/releases/fonts/font-arial-iso-8859-1.tar.bz2
# Source6-md5:	1ecd31d17b51f16332b1fcc7da36b312
Source7:	%{name}.png
Source8:	%{name}.desktop
# http://www.on2.com/gpl/mplayer/
Source9:	http://support.on2.com/gpl/mplayer/2009-10-08-mencoder-on2flixenglinux.tar.bz2
# Source9-md5:	07774a2663a8fda07c308df0c6569b56

# build (configure / Makefile) related:
Patch10:	%{name}-ldflags.patch
Patch11:	%{name}-altivec.patch
Patch12:	%{name}-check-byteswap.patch
Patch13:	%{name}-visibility-hidden-fix.patch
Patch14:	%{name}-ffmpeg.patch
Patch15:	%{name}-shared_live.patch
Patch16:	%{name}-shared.patch

# codecs, outputs, demuxers:
Patch20:	%{name}-auto-expand.patch
Patch21:	%{name}-release_directfb.patch

# goodies:
Patch30:	%{name}-cp1250-fontdesc.patch
Patch31:	%{name}-350.patch
# update, hard to fix right now because of gnome bug 579430:
# https://bugzilla.gnome.org/show_bug.cgi?id=579430
#Patch32:	%{name}-gnome-screensaver.patch

Patch100:	%{name}-on2flix.patch

URL:		http://www.mplayerhq.hu/
%{?with_directfb:BuildRequires:	DirectFB-devel}
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
%{?with_sdl:BuildRequires:	SDL-devel >= 1.1.7}
%{?with_aalib:BuildRequires:	aalib-devel}
%{?with_alsa:BuildRequires:	alsa-lib-devel}
%{?with_arts:BuildRequires:	artsc-devel}
%{?with_ssse3:BuildRequires:	binutils >= 3:2.16.92}
%{?with_cdparanoia:BuildRequires:	cdparanoia-III-devel}
%{?with_doc:BuildRequires:	docbook-style-xsl}
%{?with_doc:BuildRequires:	docbook-dtd412-xml}
BuildRequires:	dirac-devel
%{?with_dxr3:BuildRequires:	em8300-devel}
%{?with_enca:BuildRequires:	enca-devel}
%{?with_esd:BuildRequires:	esound-devel}
BuildRequires:	faac-devel
%{?with_faad:BuildRequires:	faad2-devel >= 2.0}
%{?with_system_ffmpeg:BuildRequires:	ffmpeg-devel >= 0.4.9-4.20081024.3}
BuildRequires:	freetype-devel >= 2.0.9
BuildRequires:	fribidi-devel
%{?with_vidix:BuildRequires:	vidix-devel}
%ifarch ppc
%{?with_altivec:BuildRequires:	gcc >= 5:3.3.2-3}
%endif
%{?with_gif:BuildRequires:	giflib-devel}
%{?with_gui:BuildRequires:	gtk+2-devel}
%{?with_gnomess:BuildRequires:	dbus-glib-devel}
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel}
%{?with_jack:%requires_eq	jack-audio-connection-kit-libs}
BuildRequires:	lame-libs-devel
%{?with_caca:BuildRequires:	libcaca-devel}
%{?with_libdts:BuildRequires:	libdts-devel}
%{?with_libdv:BuildRequires:	libdv-devel > 0.9.5}
%{?with_dvdnav:BuildRequires:	libdvdnav-devel >= 4.1.3}
%{?with_ggi:BuildRequires:	libggi-devel}
BuildRequires:	libjpeg-devel
%{?with_mad:BuildRequires:	libmad-devel}
BuildRequires:	libmng-devel
BuildRequires:	libmpcdec-devel >= 1.2.1
BuildRequires:	libpng-devel
%{?with_smb:BuildRequires:	libsmbclient-devel}
%{?with_theora:BuildRequires:	libtheora-devel}
%{?with_system_vorbis:BuildRequires:	libvorbis-devel}
%{?with_x264:BuildRequires:	libx264-devel >= 0.1.3}
%{?with_vdpau:BuildRequires:	libvdpau-devel}
BuildRequires:	libxslt-progs
%{?with_lirc:BuildRequires:	lirc-devel}
%{?with_live:BuildRequires:	live-devel}
%{?with_lzo:BuildRequires:	lzo-devel >= 2.0}
%{?with_nas:BuildRequires:	nas-devel}
BuildRequires:	ncurses-devel
%{?with_amr:BuildRequires:	opencore-amr-devel}
BuildRequires:	pkgconfig
%{?with_pulseaudio:BuildRequires:	pulseaudio-devel >= 0.9}
BuildRequires:	rpmbuild(macros) >= 1.527
BuildRequires:	schroedinger-devel
BuildRequires:	speex-devel >= 1.1
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRequires:	twolame-devel
%{?with_xmms:BuildRequires:	xmms-devel}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-lib-libXvMC-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
%{?with_xvid:BuildRequires:	xvid-devel >= 1:0.9.0}
%ifarch %{ix86} %{x8664}
BuildRequires:	yasm
%endif
BuildRequires:	zlib-devel
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		specflags_ia32	-fomit-frame-pointer
%if %{with altivec}
%define		specflags_ppc	-maltivec
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

%description -l de.UTF-8
MPlayer ist ein unter der freien GPL-Lizenz stehender Media-Player.
Kennzeichnend ist die herausragende Format- und
Plattform-Kompatibilität.

Es unterstützt eine Vielzahl von Video und Audio-Codecs, darunter auch
plattformexklusive, wodurch etwa Windows Media auch außerhalb von
Windows wiedergegeben werden kann. Darüber hinaus unterstützt er DVB.
Eine besondere Fehlertoleranz ermöglicht es dem mehrfach
ausgezeichneten Player, auch defekte Dateien abzuspielen. Eine weitere
Stärke ist dabei der Wegfall jeglicher Installation, so dass bereits
installierte Codecs nicht mit MPlayer kollidieren können.

%description -l es.UTF-8
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

%description -l ko.UTF-8
MPlayer는 리눅스용 무비플레이어입니다. 대부분의 mpeg, avi 그리고 asf
파일을 재생합니다. VCD, DVD, 심 지어 DivX까지 볼 수 있습니다.
MPlayer의 또 다른 큰 특징은 출력 드라이버가 다양하다는 것입니다. X11,
Xv, DGA, OpenGL, SVGAlib, fbdev와 작동하며, SDL이나
(Matrox/3dfx/Sis등의) 특정 카드에 종속된 로우레 벨 드라이버들도 사용할
수 있습니다. 대부분의 출력 드라이버들은 소프트웨어 혹은 하드웨어적인
크기조절 (scaling)을 지원하므로, 전체화면으로 영상을 감상할 수
있습니다. 뿐만아니라, 한국어, 영어, 헝가리어, 체코어, 러시아어등의
부드러운(antialiased) 자막폰트도 사용할 수 있습니다.

%description -l pl.UTF-8
Odtwarzacz wideo. Wspierane formaty wejściowe: VCD (VideoCD), MPEG1/2,
RIFF AVI, ASF 1.0, Quicktime. Wspierane kodeki audio: PCM
(nieskompresowane), MPEG layer 2/3, AC3, aLaw, MS-GSM, Win32 ACM.
Wspierane kodeki wideo: MPEG 1 and MPEG 2, Win32 ICM (VfW), OpenDivX.
Wspierane urządzenia wyjściowe: Matrox G200/G400, X11 opcjonalnie z
rozszerzeniem SHM, X11 z rozszerzeniem Xvideo, renderer OpenGL, Matrox
G400 używając framebuffera, Voodoo2/3, SDL v1.1.7 itp.

Jeśli chcesz używać kodeków win32, zainstaluj pakiet w32codec.

%description -l pt_BR.UTF-8
MPlayer é um reprodutor de filmes que suporta vários codecs de vídeo e
áudio. Diferentes mecanismos de reprodução podem também ser
escolhidos, incluindo SDL, SVGALib, frame buffer, aalib, X11 e outros.

%package -n gmplayer
Summary:	MPlayer with GTK+ GUI interface
Summary(pl.UTF-8):	MPlayer z graficznym interfejsem GTK+
Group:		X11/Applications/Multimedia
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-skin

%description -n gmplayer
MPlayer with GUI GTK+ interface.

%description -n gmplayer -l pl.UTF-8
MPlayer z graficznym interfejsem GTK+.

%package common
Summary:	Configuration files and documentation for MPlayer
Summary(pl.UTF-8):	Pliki konfiguracyjne i dokumentacja dla MPlayera
Group:		Applications/Multimedia
Suggests:	unrar
Obsoletes:	mplayer-vidix

%description common
Configuration files, man page and HTML documentation for MPlayer.

%description common -l pl.UTF-8
Pliki konfiguracyjne, strona manuala i dokumentacja HTML dla MPlayera.

%package -n mencoder
Summary:	MEncoder - a movie encoder for Linux
Summary(pl.UTF-8):	MEncoder - koder filmów dla Linuksa
Group:		Applications/Multimedia
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description -n mencoder
MEncoder is a movie encoder for Linux and is a part of the MPlayer
package.

%description -n mencoder -l pl.UTF-8
MEncoder to koder filmów dla Linuksa będący częścią pakietu MPlayer.

%prep
%setup -q -n mplayer-r%{svnver} -a3 -a6 -a9
cp -f etc/codecs.conf etc/codecs.win32.conf

# build (configure / Makefile) related:
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%{?with_system_ffmpeg:%patch14 -p1}
%{?with_live:%patch15 -p1}
%{?with_shared:%patch16 -p1}

# codecs, outputs, demuxers:
%patch20 -p1
%patch21 -p1

# goodies:
%patch30 -p0
%patch31 -p1
#%{with_gnomess:%patch32 -p1}

# on2flix
mv mencoder-on2flixenglinux{-*-*-*,}
%if %{with on2}
#%%patch100 -p1
cp -a mencoder-on2flixenglinux/patch/new_files/libmpdemux/* libmpdemux
# remove broken patches:
# - first set does not apply
# - second set beakes build
for PATCH in	asf-correct_movielength avi_check_idxflags \
		demux_lavf-add_dv_mts_preferred demux_lavf-probe_small_files \
		mencoder_07_demux_update_pts mencoder_10_correct_pts \
		mpegvideo-revert_r18381 \
		\
		reduce_spurious_logging
do
	rm mencoder-on2flixenglinux/patch/$PATCH.diff
done
for a in mencoder-on2flixenglinux/patch/*.diff; do
	patch -p0 < $a
done
%endif

# Set version
%if "x%{svnver}" != "x%{nil}"
	echo "SVN-r%{svnver}%{?with_on2:-on2}" > VERSION
%endif

cat etc/example.conf > etc/mplayer.conf
cat <<'CONFIGADD' >> etc/mplayer.conf

######################
# PLD Linux Defaults #
######################
[default]

# alternate solution for CP1250-encoded subtitles
fontconfig = yes
subcp = cp1250

# ...or if you prefer native bitmap fonts shipped with mplayer
#fontconfig = no
#subcp = iso-8859-1

# Standard location
unrarexec = "%{_bindir}/unrar"

CONFIGADD

%if %{with system_ffmpeg}
# using external ffmpeg, but mplayer adds these to includepath
rm -r libavcodec libavdevice libavformat libavutil libpostproc libswscale
%endif

# *** HOT FIXES ***

# typo, fixed in recent svn
sed 's/STREAM_NONCACHEABLE/STREAM_NON_CACHEABLE/' -i stream/stream_live555.c

# mjpeg encoder is required for Zoran hardware
sed '/_libavencoders="MPEG/s/"$/ MJPEG_ENCODER"/' -i configure

%build
CFLAGS="%{rpmcflags} -fvisibility=hidden %{?with_shared:-fvisibility=default -fPIC}"
CFLAGS="$CFLAGS -I%{_includedir}/xvid%{?with_directfb::%{_includedir}/directfb}"
%{?with_live:CFLAGS="$CFLAGS -I/usr/include/liveMedia"}

build() {
	set -x

	./configure \
	%{?debug:--enable-debug=3} \
	--prefix=%{_prefix} \
	--confdir=%{_sysconfdir}/mplayer \
	--cc="%{__cc}" \
	--extra-cflags="$CFLAGS" \
	--real-ldflags="%{rpmldflags}" \
	--extra-ldflags="%{?_x_libraries:-L%{_x_libraries}}" \
%if %{with system_ffmpeg}
	--disable-libavutil_a \
	--disable-libavcodec_a \
	--disable-libavformat_a \
	--disable-libpostproc_a \
	--enable-libavutil_so \
	--enable-libavcodec_so \
	--enable-libavformat_so \
	--enable-libpostproc_so \
%endif
%ifnarch %{ix86} %{x8664}
	--disable-mmx \
	--disable-mmxext \
	--disable-3dnow \
	--disable-3dnowext \
	--disable-sse \
	--disable-sse2 \
	--disable-fastmemcpy \
%endif
	%{__disable ssse3} \
%ifarch ppc
	%{__disable altivec} \
%endif
	%{__enable_disable amr libopencore_amrnb} %{__enable_disable amr libopencore_amrwb} \
	%{__enable_disable directfb} \
	%{__disable dxr3} \
	%{__disable ggi} \
	%{__disable live} \
	%{__disable lzo liblzo} \
	%{__disable nas} \
	%{__disable svga} \
	%{__disable aalib aa} \
	%{__disable jack} \
	%{__enable_disable alsa} \
	%{__disable arts} \
	%{__disable caca} \
	%{__disable cdparanoia} \
	%{__disable enca} \
	%{__disable esd} \
	--disable-faad-internal \
	%{__disable faad} \
	%{__disable gif} \
	%{__enable joystick} \
	%{__disable libdv} \
	%{__disable libdts libdca} \
	%{__enable_disable lirc} \
	%{__disable mad} \
	%{__disable pulseaudio pulse} \
	%{__disable quicktime qtx} \
	%{__disable real} \
	%{__enable_disable runtime runtime-cpudetection} \
	%{__disable select} \
	%{__disable smb} \
	%{__disable win32 win32dll} \
	%{__disable vorbis tremor-internal} --disable-tremor %{__disable vorbis libvorbis} \
	%{__disable_if system_vorbis tremor-internal} \
	%{__enable osd menu} \
	%{__disable theora} \
	%{__disable x264} \
	%{?with_xmms:--enable-xmms --with-xmmsplugindir=%{_libdir}/xmms/Input --with-xmmslibdir=%{_libdir}} \
	%{__disable xvid} \
	%{__disable vidix} \
	%{__disable vdpau} \
	%{__disable mencoder} \
	--enable-dga1 \
	--enable-dga2 \
	%{__enable_disable dvdnav} \
	--enable-fbdev \
	--enable-gl \
	--enable-mga \
	--enable-radio \
	--enable-radio-capture \
	%{__enable_disable sdl} \
	--enable-tdfxfb \
	--enable-vm \
	--enable-x11 \
	--enable-xmga \
	--enable-xv \
	--enable-xvmc \
	--with-xvmclib=XvMCW \
	--enable-zr \
	--enable-unrarexec \
	--enable-dynamic-plugins \
	--enable-largefiles \
	--language=all \
	--codecsdir=%{_libdir}/codecs \
	"$@"

	%{__make}
}

%if %{with gui}
# build GUI version
build --enable-gui --disable-mencoder
mv -f mplayer gmplayer
%{__make} distclean
%endif

# now build regular version
build --disable-gui

%if %{with doc}
%{__make} -j1 -C DOCS/xml
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_sysconfdir}/mplayer} \
	$RPM_BUILD_ROOT%{_mandir}/{cs,de,es,fr,hu,it,pl,sv,zh_CN,}/man1 \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/skins \
	$RPM_BUILD_ROOT%{_desktopdir}

# default config files
install etc/{codecs,mplayer%{?with_osd:,menu},input}.conf $RPM_BUILD_ROOT%{_sysconfdir}/mplayer

# executables
%if %{with mencoder}
install mencoder $RPM_BUILD_ROOT%{_bindir}/mencoder%{_suf}
ln -sf mencoder%{_suf} $RPM_BUILD_ROOT%{_bindir}/mencoder
%endif
install mplayer $RPM_BUILD_ROOT%{_bindir}/mplayer%{_suf}
ln -sf mplayer%{_suf} $RPM_BUILD_ROOT%{_bindir}/mplayer
%if %{with gui}
install gmplayer $RPM_BUILD_ROOT%{_bindir}/gmplayer%{_suf}
ln -sf gmplayer%{_suf} $RPM_BUILD_ROOT%{_bindir}/gmplayer
%endif

%if %{with shared}
install -d $RPM_BUILD_ROOT%{_libdir}
install libmplayer.so $RPM_BUILD_ROOT%{_libdir}
%endif

# fonts
cp -r font-* $RPM_BUILD_ROOT%{_datadir}/mplayer
ln -sf font-arial-iso-8859-2/font-arial-24-iso-8859-2 $RPM_BUILD_ROOT%{_datadir}/mplayer/font

%if %{with gui}
install %{SOURCE5} $RPM_BUILD_ROOT%{_desktopdir}
%endif
touch $RPM_BUILD_ROOT%{_datadir}/%{name}/skins/default
install %{SOURCE8} $RPM_BUILD_ROOT%{_desktopdir}
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
#install DOCS/man/sv/*.1 $RPM_BUILD_ROOT%{_mandir}/sv/man1
#install DOCS/man/zh/*.1 $RPM_BUILD_ROOT%{_mandir}/zh_CN/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post -n gmplayer
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun -n gmplayer
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mplayer*

%if %{with gui}
%files -n gmplayer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gmplayer*
%{_desktopdir}/gmplayer.desktop
%endif

%if %{with mencoder}
%files -n mencoder
%defattr(644,root,root,755)
%doc DOCS/tech/encoding-guide.txt DOCS/tech/encoding-tips.txt
%doc DOCS/tech/swscaler_filters.txt DOCS/tech/swscaler_methods.txt
%doc DOCS/tech/colorspaces.txt
%attr(755,root,root) %{_bindir}/mencoder*
%endif

%files common
%defattr(644,root,root,755)
%doc DOCS/tech
%{?with_shared:%attr(755,root,root) %{_libdir}/libmplayer.so}
%if %{with win32}
%doc etc/codecs.win32.conf
%endif
%if %{with doc}
# HTML and XML-generated docs
%doc DOCS/HTML/en
%lang(cs) %doc DOCS/HTML/cs
%lang(de) %doc DOCS/HTML/de
%lang(es) %doc DOCS/HTML/es
%lang(fr) %doc DOCS/HTML/fr
%lang(hu) %doc DOCS/HTML/hu
%lang(pl) %doc DOCS/HTML/pl
%lang(ru) %doc DOCS/HTML/ru
#%lang(zh_CN) %doc DOCS/zh
%endif
%doc AUTHORS README

%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*.conf
%{_mandir}/man1/*
%lang(cs) %{_mandir}/cs/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(pl) %{_mandir}/pl/man1/*
#%lang(sv) %{_mandir}/sv/man1/*
#%lang(zh_CN) %{_mandir}/zh_CN/man1/*
%{_desktopdir}/mplayer.desktop
%{_pixmapsdir}/mplayer.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/font*
%dir %{_datadir}/%{name}/skins
%ghost %{_datadir}/%{name}/skins/default
