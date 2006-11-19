#
# TODO:
# - nut support (http://www.nut.hu/ - currently down, but see svn.mplayerhq.hu/nut/)
# - update for lzo 2
# - update for pulseaudio (instead of old polypaudio)
# - use external vidix?
# - try to use external ffmpeg, lrmi and few other libs:
#   http://www.gocyberlink.com/english/products/powercinema/pcm-linux/license/mplayer-10_copyright.htm
#
# Conditional build:
%bcond_with	directfb	# with DirectFB video output
%bcond_with	dxr3		# enable use of DXR3/H+ hardware MPEG decoder
%bcond_with	ggi		# with ggi video output
%bcond_with	nas		# with NAS audio output
%bcond_with	svga		# with svgalib video output
%bcond_with	osd		# with osd menu support
%bcond_without	altivec		# without altivec support
%bcond_without	x264		# without x264 support (needs newer libx264 snap)
%bcond_with	xmms		# with XMMS inputplugin support
%bcond_without	aalib		# without aalib video output
%bcond_without	jack		# without JACKD support
%bcond_without	alsa		# without ALSA audio output
%bcond_without	arts		# without arts audio output
%bcond_without	caca		# without libcaca video output
%bcond_without	cdparanoia	# without cdparanoia support
%bcond_without	dshow		# disable DirectShow support
%bcond_without	enca		# disable using ENCA charset oracle library
%bcond_without	esd		# disable EsounD sound support
%bcond_without	faad		# disable FAAD2 (AAC) support
%bcond_without	gif		# disable GIF support
%bcond_without	gui		# without GTK+ GUI
%bcond_without	joystick	# disable joystick support
%bcond_without	libdts		# disable libdts support
%bcond_without	libdv		# disable libdv en/decoding support
%bcond_without	lirc		# without lirc support
%bcond_without	live		# without live.com libraries
%bcond_with	lzo		# with LZO support (requires lzo 1.x)
%bcond_without	mad		# without mad (audio MPEG) support
%bcond_with	polyp		# with polyp audio output (requires polypaudio 0.6 or 0.7)
%bcond_without	quicktime	# without binary quicktime dll support
%bcond_without	real		# without Real* 8/9 codecs support
%bcond_without	runtime		# disable runtime cpu detection, just detect CPU
				#  in compile time (advertised by mplayer authors as working faster); in this case
				#  mplayer may not work on machine other then where it was compiled
%bcond_without	select		# disable audio select() support (for example required this option ALSA or Vortex2 driver)
%bcond_without	smb		# disable Samba (SMB) input support
%bcond_without	theora		# without theora support
%bcond_without	win32		# without win32 codecs support
%bcond_without	vorbis		# without Ogg-Vorbis audio support
%bcond_without	xvid		# disable XviD codec
%bcond_without	mencoder	# disable mencoder (a/v encoder) compilation
%bcond_without	sdl		# disable SDL
%bcond_without	doc		# don't build docs (slow)
%bcond_with	shared		# experimental libmplayer.so support
%bcond_with	amr		# enable 3GPP Adaptive Multi Rate (AMR) speech codec support
%bcond_without	gnomess		# disable controling gnome screensaver

%ifnarch %{ix86}
%undefine	with_win32
%undefine	with_quicktime
%endif

%ifarch %{x8664}
%undefine	with_runtime
%endif

%if %{_lib} == "lib64"
%define        _suf    64
%else
%define        _suf    32
%endif

# set it to 0, or 1
%define		snapshot	0

%define		sname		MPlayer
%define		snap		%{nil}

%define		pre		rc1

Summary:	MPlayer - THE Movie Player for UN*X
Summary(de):	MPlayer ist ein unter der freien GPL-Lizenz stehender Media-Player
Summary(es):	Otro reproductor de pel�culas
Summary(ko):	�������� �̵���÷��̾�
Summary(pl):	Odtwarzacz film�w dla system�w uniksowych
Summary(pt_BR):	Reprodutor de filmes
Name:		mplayer
Version:	1.0
%define		_rel	1
Release:	3.%{pre}.%{_rel}
# DO NOT increase epoch unless it's really neccessary!
# especially such changes like pre7->pre7try2, increase Release instead!
# PS: $ rpmvercmp pre7try2 pre7
# pre7try2 > pre7
Epoch:		3
License:	GPL
Group:		Applications/Multimedia
%if %{snapshot}
#Source0:	ftp://ftp1.mplayerhq.hu/MPlayer/cvs/%{sname}-%{snap}.tar.bz2
#Source0:	%{name}-%{snap}.tar.bz2
#Source1:	libavcodec-%{snap}.tar.bz2
%else
Source0:	ftp://ftp2.mplayerhq.hu/MPlayer/releases/%{sname}-%{version}%{pre}.tar.bz2
# Source0-md5:	18c05d88e22c3b815a43ca8d7152ccdc
%endif
Source3:	ftp://ftp1.mplayerhq.hu/MPlayer/releases/fonts/font-arial-iso-8859-2.tar.bz2
# Source3-md5:	7b47904a925cf58ea546ca15f3df160c
Source5:	g%{name}.desktop
Source6:	ftp://ftp2.mplayerhq.hu/MPlayer/releases/fonts/font-arial-iso-8859-1.tar.bz2
# Source6-md5:	1ecd31d17b51f16332b1fcc7da36b312
Source7:	%{name}.png
Source8:	%{name}.desktop
Patch1:		%{name}-cp1250-fontdesc.patch
Patch2:		%{name}-codec.patch
Patch3:		%{name}-home_etc.patch
Patch4:		%{name}-350.patch
Patch5:		%{name}-configure.patch
Patch6:		%{name}-system-amr.patch
Patch8:		%{name}-altivec.patch
Patch10:	%{name}-pcmsplit.patch
Patch13:	%{name}-mythtv.patch
Patch14:	%{name}-shared.patch
#http://www.openchrome.org/snapshots/mplayer/
Patch15:	%{name}-xvmc.patch
Patch16:	%{name}-kill-mabi_altivec.patch
Patch17:	%{name}-auto-expand.patch
Patch18:	%{name}-gnome-screensaver.patch
URL:		http://www.mplayerhq.hu/
%{?with_directfb:BuildRequires:	DirectFB-devel}
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
%{?with_sdl:BuildRequires:	SDL-devel >= 1.1.7}
%{?with_aalib:BuildRequires:	aalib-devel}
%{?with_alsa:BuildRequires:	alsa-lib-devel}
%if %{with amr}
BuildRequires:	amrnb-devel
BuildRequires:	amrwb-devel	>= 5.3.0
%endif
%{?with_arts:BuildRequires:	artsc-devel}
%{?with_cdparanoia:BuildRequires:	cdparanoia-III-devel}
%{?with_doc:BuildRequires:	docbook-style-xsl}
%{?with_dxr3:BuildRequires:	em8300-devel}
%{?with_enca:BuildRequires:	enca-devel}
%{?with_esd:BuildRequires:	esound-devel}
BuildRequires:	faac-devel
%{?with_faad:BuildRequires:	faad2-devel >= 2.0}
BuildRequires:	freetype-devel
BuildRequires:	fribidi-devel
%ifarch ppc
%{?with_altivec:BuildRequires:	gcc >= 5:3.3.2-3}
%endif
%{?with_gif:BuildRequires:	giflib-devel}
%if %{with gui}
BuildRequires:	gtk+2-devel
%endif
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel}
BuildRequires:	lame-libs-devel
%{?with_caca:BuildRequires:	libcaca-devel}
%{?with_libdts:BuildRequires:	libdts-devel}
BuildRequires:	libdvdnav-devel
%{?with_libdv:BuildRequires:	libdv-devel}
%{?with_ggi:BuildRequires:	libggi-devel}
BuildRequires:	libjpeg-devel
%{?with_mad:BuildRequires:	libmad-devel}
BuildRequires:	libmpcdec-devel >= 1.2.1
BuildRequires:	libpng-devel
%{?with_smb:BuildRequires:	libsmbclient-devel}
%{?with_dshow:BuildRequires:	libstdc++-devel}
%{?with_theora:BuildRequires:	libtheora-devel}
# tremor is used by default, internal as we don't have system one
#%{?with_vorbis:BuildRequires:	libvorbis-devel}
%{?with_x264:BuildRequires:	libx264-devel >= 0.1.2-1.20060828_2245.1}
BuildRequires:	libxslt-progs
%{?with_lirc:BuildRequires:	lirc-devel}
%{?with_live:BuildRequires:	live}
%{?with_lzo:BuildRequires:	lzo-devel < 2.0}
%{?with_nas:BuildRequires:	nas-devel}
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
%{?with_polyp:BuildRequires:	polypaudio-devel >= 0.6}
%{?with_polyp:BuildRequires:	polypaudio-devel < 0.8}
BuildRequires:	speex-devel >= 1.1
%{?with_svga:BuildRequires:	svgalib-devel}
%{?with_xmms:BuildRequires:	xmms-libs}
BuildRequires:	xorg-lib-libXvMC-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
%{?with_xvid:BuildRequires:	xvid-devel >= 1:0.9.0}
BuildRequires:	zlib-devel
%{?with_gnomess:BuildRequires:	dbus-glib-devel}
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires(post,postun):	/sbin/ldconfig
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

%description -l de
MPlayer ist ein unter der freien GPL-Lizenz stehender Media-Player.
Kennzeichnend ist die herausragende Format- und
Plattform-Kompatibilit�t.

Es unterst�tzt eine Vielzahl von Video und Audio-Codecs, darunter auch
plattformexklusive, wodurch etwa Windows Media auch au�erhalb von
Windows wiedergegeben werden kann. Dar�ber hinaus unterst�tzt er DVB.
Eine besondere Fehlertoleranz erm�glicht es dem mehrfach
ausgezeichneten Player, auch defekte Dateien abzuspielen. Eine weitere
St�rke ist dabei der Wegfall jeglicher Installation, so dass bereits
installierte Codecs nicht mit MPlayer kollidieren k�nnen.

%description -l es
Reproductor video. Formatos de entrada soportados: VCD (VideoCD),
MPEG1/2, RIFF AVI, ASF 1.0, Quicktime. Codecs de audio soportados: PCM
(uncompressed), MPEG layer 2/3, AC3, aLaw, MS-GSM, Win32 ACM. Codecs
de video soportados: MPEG 1 and MPEG 2, Win32 ICM (VfW), OpenDivX.
Dispositivos de salida soportados: Matrox G200/G400 hardware, Matrox
G200/G400 overlay, X11 optionalmente con la extensi�n SHM, X11 usando
overlays con la extensi�n Xvideo, plasmador OpenGL, soporte de Matrox
G400 YUV en hardware de framebuffer de Voodoo2/3, controlador SDL
v1.1.7 etc.

Si quiere usar codecs Win32, instale el paquete w32codec.

%description -l ko
MPlayer�� �������� �����÷��̾��Դϴ�. ��κ��� mpeg, avi �׸��� asf
������ ����մϴ�. VCD, DVD, �� ���� DivX���� �� �� �ֽ��ϴ�.
MPlayer�� �� �ٸ� ū Ư¡�� ��� ����̹��� �پ��ϴٴ� ���Դϴ�. X11,
Xv, DGA, OpenGL, SVGAlib, fbdev�� �۵��ϸ�, SDL�̳�
(Matrox/3dfx/Sis����) Ư�� ī�忡 ���ӵ� �ο췹 �� ����̹��鵵 �����
�� �ֽ��ϴ�. ��κ��� ��� ����̹����� ����Ʈ���� Ȥ�� �ϵ��������
ũ������ (scaling)�� �����ϹǷ�, ��üȭ������ ������ ������ ��
�ֽ��ϴ�. �Ӹ��ƴ϶�, �ѱ���, ����, �밡����, ü�ھ�, ���þƾ����
�ε巯��(antialiased) �ڸ���Ʈ�� ����� �� �ֽ��ϴ�.

%description -l pl
Odtwarzacz wideo. Wspierane formaty wej�ciowe: VCD (VideoCD), MPEG1/2,
RIFF AVI, ASF 1.0, Quicktime. Wspierane kodeki audio: PCM
(nieskompresowane), MPEG layer 2/3, AC3, aLaw, MS-GSM, Win32 ACM.
Wspierane kodeki wideo: MPEG 1 and MPEG 2, Win32 ICM (VfW), OpenDivX.
Wspierane urz�dzenia wyj�ciowe: Matrox G200/G400, X11 opcjonalnie z
rozszerzeniem SHM, X11 z rozszerzeniem Xvideo, renderer OpenGL, Matrox
G400 u�ywaj�c framebuffera, Voodoo2/3, SDL v1.1.7 itp.

Je�li chcesz u�ywa� kodek�w win32, zainstaluj pakiet w32codec.

%description -l pt_BR
MPlayer � um reprodutor de filmes que suporta v�rios codecs de v�deo e
�udio. Diferentes mecanismos de reprodu��o podem tamb�m ser
escolhidos, incluindo SDL, SVGALib, frame buffer, aalib, X11 e outros.

%package -n gmplayer
Summary:	MPlayer with GTK+ GUI interface
Summary(pl):	MPlayer z graficznym interfejsem GTK+
Group:		X11/Applications/Multimedia
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-skin
Provides:	%{name} = %{epoch}:%{version}-%{release}

%description -n gmplayer
MPlayer with GUI GTK+ interface.

%description -n gmplayer -l pl
MPlayer z graficznym interfejsem GTK+.

%package common
Summary:	Configuration files and documentation for MPlayer
Summary(pl):	Pliki konfiguracyjne i dokumentacja dla MPlayera
Group:		Applications/Multimedia

%description common
Configuration files, man page and HTML documentation for MPlayer.

%description common -l pl
Pliki konfiguracyjne, strona manuala i dokumentacja HTML dla MPlayera.

%package -n mencoder
Summary:	MEncoder - a movie encoder for Linux
Summary(pl):	MEncoder - koder film�w dla Linuksa
Group:		Applications/Multimedia
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description -n mencoder
MEncoder is a movie encoder for Linux and is a part of the MPlayer
package.

%description -n mencoder -l pl
MEncoder to koder film�w dla Linuksa b�d�cy cz�ci� pakietu MPlayer.

%prep
%if %{snapshot}
%setup -q -n %{name}-%{snap} -a 1 -a 3 -a 6
%else
%setup -q -n %{sname}-%{version}%{pre} -a 3 -a 6
%endif

cp -f etc/codecs.conf etc/codecs.win32.conf
%patch1 -p0
##%patch2 -p1
##%patch3 -p1	-- old home_etc behavior
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch8 -p1
#%%patch10 -p1
#%patch13 -p1	# TODO
%if %{with shared}
%patch14 -p1
%endif
#%patch15 -p0	# TODO
%patch16 -p1
%patch17 -p1
%if %{with gnomess}
%patch18 -p1
%endif

%if %{with snapshot}
find . -type d -name CVS -print | xargs rm -rf
%endif

%build
%if %{with shared}
CFLAGS="%{rpmcflags} -fPIC"
%else
CFLAGS="%{rpmcflags}"
%endif
CC="%{__cc}"
LDFLAGS="%{rpmldflags}"
export CC CFLAGS LDFLAGS

build() {
set -x
	./configure \
	%{?debug:--enable-debug=3} \
	--prefix=%{_prefix} \
	--confdir=%{_sysconfdir}/mplayer \
	--with-x11libdir=%{_libdir} \
	--with-extraincdir=%{_includedir}/xvid \
	--enable-menu \
%ifnarch %{ix86} %{x8664}
	--disable-mmx \
	--disable-mmxext \
	--disable-3dnow \
	--disable-3dnowext \
	--disable-sse \
	--disable-sse2 \
	--disable-fastmemcpy \
%endif
%ifarch ppc
%{!?with_altivec:--disable-altivec} \
%endif
%{!?with_amr:--disable-amr_nb --disable-amr_wb} \
%{?with_amr:--enable-amr_nb --enable-amr_wb} \
%{?with_directfb:--enable-directfb} \
%{!?with_directfb:--disable-directfb} \
%{!?with_dxr3:--disable-dxr3} \
%{!?with_ggi:--disable-ggi} \
%{?with_live:--enable-live --with-livelibdir=%{_libdir}/liveMedia --with-extraincdir=/usr/include/liveMedia} \
%{!?with_live:--disable-live} \
%{!?with_lzo:--disable-liblzo} \
%{!?with_nas:--disable-nas} \
%{!?with_svga:--disable-svga} \
%{!?with_aalib:--disable-aa} \
%{!?with_jack:--disable-jack} \
%{!?with_alsa:--disable-alsa} \
%{?with_alsa:--enable-alsa --disable-select} \
%{!?with_arts:--disable-arts} \
%{!?with_caca:--disable-caca} \
%{!?with_cdparanoia:--disable-cdparanoia} \
%{!?with_dshow:--disable-dshow} \
%{!?with_enca:--disable-enca} \
%{!?with_esd:--disable-esd} \
%{!?with_faad:--disable-faad-external --disable-faad-internal} \
%{?with_faad:--disable-faad-internal} \
%{!?with_gif:--disable-gif} \
%{?with_joystick:--enable-joystick} \
%{!?with_libdv:--disable-libdv} \
%{!?with_libdts:--disable-libdts} \
--%{?with_lirc:en}%{!?with_lirc:dis}able-lirc \
%{!?with_mad:--disable-mad} \
%{!?with_polyp:--disable-polyp} \
%{!?with_quicktime:--disable-qtx} \
%{!?with_real:--disable-real} \
--%{?with_runtime:en}%{!?with_runtime:dis}able-runtime-cpudetection \
%{!?with_select:--disable-select} \
%{!?with_smb:--disable-smb} \
%{!?with_win32:--disable-win32} \
%{!?with_vorbis:--disable-vorbis} \
%{?with_osd:--enable-menu} \
%{!?with_theora:--disable-theora} \
%{!?with_x264:--disable-x264} \
%{?with_xmms:--enable-xmms --with-xmmsplugindir=%{_libdir}/xmms/Input --with-xmmslibdir=%{_libdir}} \
%{!?with_xvid:--disable-xvid} \
%{!?with_mencoder:--disable-mencoder} \
	--enable-dga \
	--enable-fbdev \
	--enable-gl \
	--enable-mga \
	--%{?with_sdl:en}%{!?with_sdl:dis}able-sdl \
	--enable-tdfxfb \
	--enable-vm \
	--enable-x11 \
	--enable-xmga \
	--enable-xv \
	--enable-xvmc \
	--enable-dynamic-plugins \
	--enable-largefiles \
	--language=all \
	--with-codecsdir=%{_libdir}/codecs \
	--with-xvmclib=XvMCW \
	"$@"

	%{__make}
}

%if %{with gui}
# build GUI version
build --enable-gui
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
	$RPM_BUILD_ROOT{%{_datadir}/mplayer/Skin,%{_libdir}/mplayer/vidix} \
	$RPM_BUILD_ROOT%{_desktopdir}

# default config files
sed -e '/Delete this default/d' etc/example.conf > etc/mplayer.conf
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

# fonts
rm -f font-*/runme
cp -r font-* $RPM_BUILD_ROOT%{_datadir}/mplayer
ln -sf font-arial-iso-8859-2/font-arial-24-iso-8859-2 $RPM_BUILD_ROOT%{_datadir}/mplayer/font

# libraries
%ifarch %{ix86}
install libdha/libdha.so.1.0 $RPM_BUILD_ROOT%{_libdir}
install vidix/drivers/*.so $RPM_BUILD_ROOT%{_libdir}/mplayer/vidix
%endif

%if %{with gui}
ln -s Blue $RPM_BUILD_ROOT%{_datadir}/%{name}/Skin/default
%endif

# X-files
%if %{with gui}
install %{SOURCE5} $RPM_BUILD_ROOT%{_desktopdir}
%endif
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
%attr(755,root,root) %{_bindir}/mplayer*

%if %{with gui}
%files -n gmplayer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gmplayer*
%{_desktopdir}/gmplayer.desktop
%dir %{_datadir}/%{name}/Skin
%ghost %{_datadir}/%{name}/Skin/default
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
# HTML and XML-generated docs
%doc DOCS/HTML/en
%doc DOCS/tech
%if %{with win32}
%doc etc/codecs.win32.conf
%endif
%lang(cs) %doc DOCS/HTML/cs
%lang(de) %doc DOCS/HTML/de
%lang(es) %doc DOCS/HTML/es
%lang(fr) %doc DOCS/HTML/fr
%lang(hu) %doc DOCS/HTML/hu
%lang(pl) %doc DOCS/HTML/pl
%lang(ru) %doc DOCS/HTML/ru
%lang(zh_CN) %doc DOCS/zh
%doc AUTHORS ChangeLog README

%ifarch %{ix86}
%attr(755,root,root) %{_libdir}/libdha.so.*.*
%attr(755,root,root) %{_libdir}/mplayer
%endif
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
%lang(sv) %{_mandir}/sv/man1/*
%lang(zh_CN) %{_mandir}/zh_CN/man1/*
%{_desktopdir}/mplayer.desktop
%{_pixmapsdir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/font*
