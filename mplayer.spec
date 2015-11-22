#
# Conditional build:
# - CPU optimization:
%bcond_without	altivec		# PPC altivec support
%bcond_without	ssse3		# SSSE3 optimizations (needs binutils >= 2.16.92)
%bcond_without	runtime		# disable runtime cpu detection, just detect CPU
				#  in compile time (advertised by mplayer authors as working faster); in this case
				#  mplayer may not work on machine other then where it was compiled
%bcond_without	hidden_visibility	# no gcc hidden visibility
%bcond_without	verbose		# disable verbose build
# - general features:
%bcond_without	bluray		# Blu-ray support
%bcond_without	cdio		# libcdio support
%bcond_without	cdparanoia	# cdparanoia support (when libcdio not enabled)
%bcond_without	doc		# don't build docs (slow)
%bcond_without	dvdnav		# dvdnav support
%bcond_without	system_dvdcss	# system libdvdcss library (instead of internal copy)
%bcond_without	system_dvdread	# system libdvdread library (instead of internal copy)
%bcond_without	enca		# disable using ENCA charset oracle library
%bcond_without	gui		# without GTK+ GUI
%bcond_without	joystick	# joystick support
%bcond_without	lirc		# lirc support
%bcond_without	live		# LIVE555 Streaming Media support
%bcond_without	mencoder	# mencoder (a/v encoder) compilation
%bcond_without	nemesi		# NeMeSi Streaming Media support
%bcond_with	on2		# patches from On2 Flix Engine for Linux
%bcond_without	osd		# osd menu support
%bcond_without	rtmp		# RTMPDump Streaming Media support
%bcond_with	shared		# experimental libmplayer.so support
%bcond_without	smb		# Samba (SMB) input support
%bcond_without	vstream		# TiVo vstream client support
# - codecs:
%bcond_without	amr		# Adaptive Multi Rate (AMR) speech codec support
%bcond_without	bs2b		# BS2B audio filter support
%bcond_without	crystalhd	# CrystalHD support
%bcond_without	faad		# FAAD2 (AAC) support
%bcond_without	gif		# GIF support
%bcond_without	ladspa		# LADSPA plugin support
%bcond_without	libdts		# libdts support
%bcond_without	libdv		# libdv en/decoding support
%bcond_without	lzo		# LZO support (requires lzo 2.x)
%bcond_without	mad		# mad (audio MPEG) support
%bcond_without	mpg123		# libmpg123 MP3 decoding support
%bcond_with	musepack	# libmpcdec support (deprecated in favour of libavcodec)
%bcond_without	openjpeg	# OpenJPEG (JPEG2000) input/output support
%bcond_without	quicktime	# binary quicktime dll support
%bcond_without	real		# Real* 8/9 codecs support
%bcond_without	vorbis		# Ogg Vorbis audio support (both tremor and libvorbis)
%bcond_with	tremor		# use tremor instead of libvorbis
%bcond_without	theora		# Ogg Theora video support
%bcond_without	win32		# Win32 codecs support
%bcond_without	x264		# x264 support
%bcond_with	xmms		# XMMS inputplugin support
%bcond_without	xvid		# XviD codec
%bcond_with	system_libmpeg2	# system libmpeg2 library (instead of internal copy with some quantizer modifications)
%bcond_with	system_ffmpeg	# use ffmpeg-devel, rather bundled sources (likely needs ffmpeg from same svn revision than mplayer)
# - video output:
%bcond_without	aalib		# aalib video output
%bcond_without	caca		# libcaca video output
%bcond_with	directfb	# DirectFB video output
%bcond_with	dxr2		# DXR2 (hardware MPEG decoder) video output
%bcond_with	dxr3		# DXR3/H+ (hardware MPEG decoder) video output
%bcond_with	ggi		# GGI video output
%bcond_without	sdl		# SDL video output
%bcond_with	svga		# svgalib video output
%bcond_without	vdpau		# VDPAU acceleration
%bcond_without	vidix		# VIDIX video drivers
%bcond_with	zr		# ZR360[56]7/ZR36060 video output (needs deprecated V4L1 linux headers)
%bcond_with	gnomess		# controling gnome screensaver [patch not updated]
# - audio output:
%bcond_without	alsa		# ALSA audio output
%bcond_with	arts		# aRts audio output
%bcond_with	esd		# EsounD sound support
%bcond_without	jack		# JACKD support
%bcond_with	nas		# NAS audio output
%bcond_without	pulseaudio	# pulseaudio output
%bcond_without	select		# audio select() support (required e.g. for ALSA or Vortex2 driver)

%if %{with alsa}
%undefine	with_select
%endif
%if %{without vorbis}
%undefine	with_tremor
%endif

%ifnarch %{ix86}
%undefine	with_win32
%undefine	with_quicktime
%undefine	with_vidix
%endif
%ifnarch %{ix86} %{x8664} ppc ppc64
%undefine	with_runtime
%endif
%ifnarch %{ix86} %{x8664}
%undefine	with_vdpau
%endif
%ifnarch ppc
%undefine	with_altivec
%endif
%ifnarch i686 pentium4 athlon %{x8664}
%undefine	with_crystalhd
%endif

%if %{_lib} != "lib"
%define		binsuf	%(lib=%{_lib} ; echo ${lib#lib})
%else
%ifarch	%{ix86} ppc sparc sparcv9 s390
%define		binsuf	32
%else
%define		binsuf	%{nil}
%endif
%endif

# date from directory inside of tarball (like mplayer-export-2014-04-29)
%define	snap	2015-11-22
%define	ssnap	%(echo %{snap} | tr -d -)
%define	rel	1
Summary:	MPlayer - THE Movie Player for UN*X
Summary(de.UTF-8):	MPlayer ist ein unter der freien GPL-Lizenz stehender Media-Player
Summary(es.UTF-8):	Otro reproductor de películas
Summary(ko.UTF-8):	리눅스용 미디어플레이어
Summary(pl.UTF-8):	Odtwarzacz filmów dla systemów uniksowych
Summary(pt_BR.UTF-8):	Reprodutor de filmes
Name:		mplayer
Version:	1.2
Release:	1.%{ssnap}.%{rel}
# DO NOT increase epoch unless it's really neccessary!
# especially such changes like pre7->pre7try2, increase Release instead!
# PS: $ rpmvercmp pre7try2 pre7
# pre7try2 > pre7
Epoch:		3
License:	GPL
Group:		Applications/Multimedia
# Source0:        http://mplayerhq.hu/MPlayer/releases/MPlayer-%{version}.tar.xz
Source0:	ftp://ftp.mplayerhq.hu/MPlayer/releases/mplayer-export-snapshot.tar.bz2
# Source0-md5:	e579ef10c11ff52502b567ad6d6d1a07
Source1:	http://ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2
# Source1-md5:	51b6a0d63c6943e7e1322752c3039857
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

Patch15:	%{name}-live555-async.patch

Patch17:	%{name}-gsm.patch
Patch18:	%{name}-openjpeg.patch
Patch19:	%{name}-shared.patch
Patch20:	%{name}-vstream.patch

# codecs, outputs, demuxers:
Patch21:	%{name}-auto-expand.patch
Patch22:	%{name}-release_directfb.patch

# goodies:
Patch30:	%{name}-cp1250-fontdesc.patch
Patch31:	%{name}-350.patch
# update, hard to fix right now because of gnome bug 579430:
# https://bugzilla.gnome.org/show_bug.cgi?id=579430
#Patch32:	%{name}-gnome-screensaver.patch

Patch100:	%{name}-on2flix.patch
Patch101:	%{name}-link.patch

URL:		http://www.mplayerhq.hu/
%{?with_directfb:BuildRequires:	DirectFB-devel >= 0.9.22}
BuildRequires:	EGL-devel
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-GLX-devel
%{?with_sdl:BuildRequires:	SDL-devel >= 1.1.7}
# checked, but seems actually not used
#%{?with_sdl:BuildRequires:	SDL_image-devel}
BuildRequires:	a52dec-libs-devel
%{?with_aalib:BuildRequires:	aalib-devel}
%{?with_alsa:BuildRequires:	alsa-lib-devel}
%{?with_arts:BuildRequires:	artsc-devel}
BuildRequires:	binutils >= 2.10.1
%{?with_ssse3:BuildRequires:	binutils >= 3:2.16.92}
BuildRequires:	bzip2-devel
#%{?with_cdparanoia:BuildRequires:	cdparanoia-III-devel}
%{?with_gnomess:BuildRequires:	dbus-glib-devel}
BuildRequires:	dirac-devel
%{?with_doc:BuildRequires:	docbook-dtd412-xml}
%{?with_doc:BuildRequires:	docbook-style-xsl}
%{?with_dxr2:BuildRequires:	dxr2-driver-devel}
%{?with_dxr3:BuildRequires:	em8300-devel}
%{?with_enca:BuildRequires:	enca-devel}
%{?with_esd:BuildRequires:	esound-devel}
BuildRequires:	faac-devel
%{?with_faad:BuildRequires:	faad2-devel >= 2.0}
%{?with_system_ffmpeg:BuildRequires:	ffmpeg-devel >= 0.4.9-4.20081024.3}
BuildRequires:	fontconfig-devel >= 1:2.4.2
BuildRequires:	freetype-devel >= 1:2.2.1
BuildRequires:	fribidi-devel
%{?with_altivec:BuildRequires:	gcc >= 5:4.1}
%{?with_gif:BuildRequires:	giflib-devel}
%{?with_gui:BuildRequires:	glib2-devel >= 1:2.6.0}
BuildRequires:	gnutls-devel
%{?with_gui:BuildRequires:	gtk+2-devel >= 2:2.4.0}
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel}
%{?with_ladspa:BuildRequires:	ladspa-devel}
BuildRequires:	lame-libs-devel
BuildRequires:	libass-devel >= 0.9.10
%{?with_bluray:BuildRequires:	libbluray-devel}
%{?with_bs2b:BuildRequires:	libbs2b-devel >= 3.0.0}
%{?with_caca:BuildRequires:	libcaca-devel}
%{?with_cdio:BuildRequires:	libcdio-paranoia-devel}
%{?with_crystalhd:BuildRequires:	libcrystalhd-devel}
%{?with_libdts:BuildRequires:	libdts-devel}
%{?with_libdv:BuildRequires:	libdv-devel > 0.9.5}
#%{?with_system_dvdcss:BuildRequires:	libdvdcss-devel}
%{?with_dvdnav:BuildRequires:	libdvdnav-devel >= 4.1.3}
%{?with_system_dvdread:BuildRequires:	libdvdread-devel >= 4.1}
%{?with_ggi:BuildRequires:	libggi-devel}
%{?with_ggi:BuildRequires:	libggiwmh-devel}
BuildRequires:	libgsm-devel
BuildRequires:	libjpeg-devel
%{?with_mad:BuildRequires:	libmad-devel}
BuildRequires:	libmng-devel
%{?with_musepack:BuildRequires:	libmpcdec-devel >= 1.2.1}
%{?with_system_libmpeg2:BuildRequires:	libmpeg2-devel}
%{?with_mpg123:BuildRequires:	libmpg123-devel >= 1.14}
%{?with_nemesi:BuildRequires:	libnemesi-devel >= 0.6.3}
BuildRequires:	libnut-devel
BuildRequires:	libpng-devel
%{?with_rtmp:BuildRequires:	librtmp-devel}
%{?with_smb:BuildRequires:	libsmbclient-devel}
%{?with_theora:BuildRequires:	libtheora-devel}
%{?with_vdpau:BuildRequires:	libvdpau-devel}
%if %{with vorbis} && %{without tremor}
BuildRequires:	libvorbis-devel
%endif
BuildRequires:	libvpx-devel
# build >= 118
%{?with_x264:BuildRequires:	libx264-devel >= 0.1.3}
BuildRequires:	libxslt-progs
# with v4l2 headers
BuildRequires:	linux-libc-headers >= 7:2.6.22
%{?with_lirc:BuildRequires:	lirc-devel}
%{?with_live:BuildRequires:	live-devel >= 2:2011.01.10}
%{?with_lzo:BuildRequires:	lzo-devel >= 2.0}
%{?with_nas:BuildRequires:	nas-devel}
BuildRequires:	ncurses-devel
%{?with_amr:BuildRequires:	opencore-amr-devel}
%{?with_openjpeg:BuildRequires:	openjpeg-devel}
BuildRequires:	opus-devel
BuildRequires:	pkgconfig
%{?with_pulseaudio:BuildRequires:	pulseaudio-devel >= 0.9}
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.527
BuildRequires:	schroedinger-devel
BuildRequires:	speex-devel >= 1.1
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRequires:	tar >= 1:1.22
%{?with_tremor:BuildRequires:	tremor-devel}
BuildRequires:	twolame-devel
%{?with_vidix:BuildRequires:	vidix-devel}
%{?with_vstream:BuildRequires:	vstream-client-devel}
BuildRequires:	webrtc-libilbc-devel
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
BuildRequires:	xz
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

%package doc
Summary:	HTML documentation for MPlayer
Summary(pl.UTF-8):	Dokumentacja do MPlayera w formacie HTML
Group:		Documentation

%description doc
HTML Documentation for MPlayer.

%description doc -l pl.UTF-8
Dokumentacja do MPlayera w formacie HTML.

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
%setup -q -n %{name}-export-%{snap} -a1 -a3 -a6 -a9
cp -f etc/codecs.conf etc/codecs.win32.conf

# build (configure / Makefile) related:
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%patch15 -p1

%patch17 -p1
%patch18 -p1
%{?with_shared:%patch19 -p1}
%patch20 -p1

# codecs, outputs, demuxers:
%patch21 -p1
%patch22 -p1

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

%patch101 -p1

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

# Joystick input is disabled because of issues on some laptops (thinkpad, macbook pro).
joystick=no

CONFIGADD

%if %{with system_ffmpeg}
# using external ffmpeg, but mplayer adds these to includepath
%{__rm} -rf ffmpeg
%endif

%build
CFLAGS="%{rpmcflags} %{?with_hidden_visibility:-fvisibility=hidden} %{?with_shared:-fvisibility=default -fPIC}"
CFLAGS="$CFLAGS -I%{_includedir}/xvid%{?with_directfb::%{_includedir}/directfb} -DHAVE_GSM_H=1"

# NOTE:
# - lircc refers to obsolete liblircc library (used in LIRCCD < 0.9)
# - toolame is obsolete predecessor of twolame
# - libcdio-paranoia is preferred over cdparanoia-III libs
build() {
	set -x

	./configure \
	%{?debug:--enable-debug=3} \
	--prefix=%{_prefix} \
	--codecsdir=%{_libdir}/codecs \
	--confdir=%{_sysconfdir}/mplayer \
	--cc="%{__cc}" \
	--extra-cflags="$CFLAGS" \
	--real-ldflags="%{rpmldflags}" \
	--extra-ldflags="%{?_x_libraries:-L%{_x_libraries}}" \
	--language=all \
%if %{with system_ffmpeg}
	--disable-ffmpeg_a \
%endif
%ifnarch %{ix86} %{x8664}
	--disable-3dnow \
	--disable-3dnowext \
	--disable-fastmemcpy \
	--disable-mmx \
	--disable-mmxext \
	--disable-sse \
	--disable-sse2 \
%endif
	%{__disable ssse3} \
%ifarch ppc
	%{__disable altivec} \
%endif
	%{__disable aalib aa} \
	%{__enable_disable alsa} \
	%{__disable arts} \
	%{__disable bluray} \
	%{__disable caca} \
	%{__disable cdparanoia} \
	--enable-dga1 \
	--enable-dga2 \
	%{__enable_disable directfb} \
	%{__enable_disable dvdnav} \
	%{__disable system_dvdread dvdread-internal} \
	%{__disable dxr2} \
	%{__disable dxr3} \
	--enable-dynamic-plugins \
	%{__disable enca} \
	%{__disable esd} \
	%{__disable faad} \
	--enable-fbdev \
	%{__disable gif} \
	--enable-gl \
	%{__disable ggi} \
	%{__disable jack} \
	%{__enable joystick} \
	%{__disable cdio libcdio} \
	%{__disable ladspa} \
	%{__disable bs2b libbs2b} \
	%{__disable libdts libdca} \
	%{__disable libdv} \
	%{__disable system_dvdcss libdvdcss-internal} \
	%{__disable lzo liblzo} \
	%{__disable system_libmpeg2 libmpeg2-internal} \
	%{__disable nemesi} \
	%{__enable_disable amr libopencore_amrnb} %{__enable_disable amr libopencore_amrwb} \
	%{__disable openjpeg} \
	%{__disable rtmp librtmp} \
	%{__disable vorbis libvorbis} \
	%{__enable_disable lirc} \
	--disable-lircc \
	%{__disable live} \
	%{__disable mad} \
	%{__disable mencoder} \
	%{__enable osd menu} \
	--enable-mga \
	%{__disable mpg123} \
	%{__enable musepack} \
	%{__disable nas} \
	%{__disable pulseaudio pulse} \
	%{__disable quicktime qtx} \
	--enable-radio \
	--enable-radio-capture \
	%{__disable real} \
	%{__enable_disable runtime runtime-cpudetection} \
	%{__enable_disable sdl} \
	%{__disable select} \
	--enable-s3fb \
	%{__disable smb} \
	%{__disable svga} \
	--enable-tdfxfb \
	--enable-tdfxvid \
	%{__disable theora} \
	--disable-toolame \
	%{!?with_tremor:--disable-tremor} \
	--enable-unrarexec \
	%{__disable vdpau} \
	%{__disable vidix} \
	%{__disable vstream} \
	--enable-vm \
%ifarch ppc
	--enable-wii \
%endif
	%{__disable win32 win32dll} \
	--enable-x11 \
	%{__disable x264} \
	--enable-xmga \
	%{?with_xmms:--enable-xmms --with-xmmsplugindir=%{_libdir}/xmms/Input --with-xmmslibdir=%{_libdir}} \
	--enable-xv \
	%{__disable xvid} \
	--enable-xvmc --with-xvmclib=XvMCW \
	%{__enable_disable zr} \
	"$@"

	%{__make} %{?with_verbose:V=1}
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
%{__make} -j1 doc
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_sysconfdir}/mplayer} \
	$RPM_BUILD_ROOT%{_mandir}/{cs,de,es,fr,hu,it,pl,ru,sv,zh_CN,}/man1 \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/skins \
	$RPM_BUILD_ROOT%{_desktopdir}

# default config files
install etc/{codecs,mplayer%{?with_osd:,menu},input}.conf $RPM_BUILD_ROOT%{_sysconfdir}/mplayer

# executables
for prog in mplayer %{?with_mencoder:mencoder} %{?with_gui:gmplayer} ; do
install $prog $RPM_BUILD_ROOT%{_bindir}/${prog}%{binsuf}
%if "%{binsuf}" != ""
ln -sf ${prog}%{binsuf} $RPM_BUILD_ROOT%{_bindir}/$prog
%endif
done

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
install DOCS/man/ru/*.1 $RPM_BUILD_ROOT%{_mandir}/ru/man1
#install DOCS/man/sv/*.1 $RPM_BUILD_ROOT%{_mandir}/sv/man1
install DOCS/man/zh_CN/*.1 $RPM_BUILD_ROOT%{_mandir}/zh_CN/man1

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

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%doc DOCS/tech
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

%files common
%defattr(644,root,root,755)
%doc AUTHORS README
%{?with_shared:%attr(755,root,root) %{_libdir}/libmplayer.so}
%if %{with win32}
%doc etc/codecs.win32.conf
%endif

%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*.conf
%{_mandir}/man1/mplayer.1*
%lang(cs) %{_mandir}/cs/man1/mplayer.1*
%lang(de) %{_mandir}/de/man1/mplayer.1*
%lang(es) %{_mandir}/es/man1/mplayer.1*
%lang(fr) %{_mandir}/fr/man1/mplayer.1*
%lang(hu) %{_mandir}/hu/man1/mplayer.1*
%lang(it) %{_mandir}/it/man1/mplayer.1*
%lang(pl) %{_mandir}/pl/man1/mplayer.1*
%lang(ru) %{_mandir}/ru/man1/mplayer.1*
#%lang(sv) %{_mandir}/sv/man1/mplayer.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/mplayer.1*
%{_desktopdir}/mplayer.desktop
%{_pixmapsdir}/mplayer.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/font*
%dir %{_datadir}/%{name}/skins
%ghost %{_datadir}/%{name}/skins/default
