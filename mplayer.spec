#
# Conditional build:
# _with_3dnow		- with 3Dnow! support (AMD K6,K7)
# _with_3dnowex		- with 3Dnow-dsp! support (AMD K7)
# _with_sse		- with SSE support (Pentium III+)
# _with_mmx		- with MMX support
# _with_mmx2		- with MMX2 support (Pentium III+,AMD K7)
# _with_ggi		- with ggi video output
# _without_alsa		- without ALSA support
# _without_arts		- without arts support
# _without_lirc		- without lirc support
# _without_vorbis	- without ogg-vorbis support
# _with_divx4linux	- with divx4linux support (binaries, instead of included OpenDivx)
# _without_select	- disable audio select() support ( for example required this option ALSA or Vortex2 driver )
# _without_win32	- disable requirement for win32 codecs (req: w23codec)
#

%define sname	MPlayer
%define snap 	20010902
%define ffmpeg_ver 	0.4.5

%ifnarch %{ix86}
%define _without_win32 1
%endif

Summary:	Yet another movie player for linux
Summary(pl):	Jeszcze jeden odtwarzacz filmów dla Linuksa
Name:		mplayer
Version:	0.18.%{snap}
Release:	10
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://www.mplayerhq.hu/${sname}/cvs/%{sname}-%{snap}.tar.bz2
Source1:	http://prdownloads.sourceforge.net/ffmpeg/ffmpeg-%{ffmpeg_ver}.tar.gz
Source2:	%{name}.conf
Patch0:		%{name}-make.patch
Patch1:		%{name}-confpath.patch
Patch2:		%{name}-codecs_no_w32.patch
URL:		http://mplayer.sourceforge.net/
%{!?_without_win32:Requires:	w32codec}
Requires:	OpenGL
BuildRequires:	SDL-devel >= 1.1.7
BuildRequires:	XFree86-devel >= 4.0.2
BuildRequires:	OpenGL-devel
BuildRequires:	ncurses-devel
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
%{!?_without_arts:BuildRequires:	arts-devel}
%{!?_without_vorbis:BuildRequires:	libvorbis-devel}
%{?_with_divx4linux:BuildRequires:	divx4linux-devel}
%{?_with_ggi:BuildRequires:		libggi-devel}
BuildRequires:	esound-devel
BuildRequires:	audiofile-devel
%{!?_without_lirc:BuildRequires:	lirc-devel}
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc

%description
Movie player for linux. Supported input formats: VCD (VideoCD),
MPEG1/2, RIFF AVI, ASF 1.0. Supported audio codecs: PCM
(uncompressed), MPEG layer 2/3, AC3, aLaw, MS-GSM, Win32 ACM.
Supported video codecs: MPEG 1 and MPEG 2, Win32 ICM (VfW), OpenDivX.
Supported output devices: Matrox G200/G400 hardware, Matrox G200/G400
overlay, X11 optionally with SHM extension, X11 using overlays with
the Xvideo extension, OpenGL renderer, Matrox G400 YUV support on
framebuffer Voodoo2/3 hardware, SDL v1.1.7 driver etc.

%description -l pl
Odtwarzacz wideo dla Linuksa. Wspierane formaty wej¶ciowe: VCD
(VideoCD), MPEG1/2, RIFF AVI, ASF 1.0. Wspierane kodeki audio: PCM
(nieskompresowane), MPEG layer 2/3, AC3, aLaw, MS-GSM, Win32 ACM.
Wspierane kodeki wideo: MPEG 1 and MPEG 2, Win32 ICM (VfW), OpenDivX.
Wspierane urz±dzenia wyj¶ciowe: Matrox G200/G400, X11 opcjonalnie z
rozszerzeniem SHM, X11 z rozszerzeniem Xvideo, renderer OpenGL, Matrox
G400 u¿ywaj±c framebuffera, Voodoo2/3, SDL v1.1.7 itp.

%prep
%setup  -q -n %{sname}-%{snap} -a 1
%patch0 -p1
%patch1 -p1
%{?_without_win32:%patch2 -p1}

cp -ar ffmpeg/libavcodec/* libavcodec

%build
CFLAGS="%{rpmcflags} -I/usr/X11R6/include" \
%configure \
			--with-win32libdir="/usr/lib/win32" \
			--disable-kernel-extchk \
%{?_with_divx4linux:	--with-extraincdir=/usr/include/divx} \
%ifarch i586 i686
%{?_with_mmx:		--enable-mmx} \
%{?_with_3dnow:		--enable-3dnow} \
%{?_with_3dnowex:	--enable-3dnowex} \
%{?_with_sse:		--enable-sse} \
%{?_with_mmx2:		--enable-mmx2} \
%endif
%ifarch i686		
			--enable-mtrr \
%else
			--disable-mtrr \
%endif
%{!?_without_alsa:	--enable-alsa --disable-select} \
%{?_without_alsa:	--disable-alsa} \
			--enable-gl \
			--enable-dga \
			--enable-xv \
			--enable-vm \
			--enable-x11 \
			--enable-mga \
			--enable-xmga \
			--enable-sdl \
			--enable-fbdev \
			--enable-termcap \
			--enable-esd \
%{?_with_ggi:		--enable-ggi} \
%{!?_with_ggi:		--disable-ggi} \
%{?_with_divx4linux:	--enable-divx4} \
%{!?_with_divx4linux:	--disable-divx4} \
%{!?_without_lirc:	--enable-lirc} \
%{?_without_lirc:	--disable-lirc} \
%{!?_without_vorbis:	--enable-oggvorbis} \
%{?_without_vorbis:	--disable-oggvorbis} \
%{?_without_select:	--disable-select} \
%{?_without_win32:	--disable-win32}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}/mplayer}

install mplayer		$RPM_BUILD_ROOT%{_bindir}
install DOCS/*.1	$RPM_BUILD_ROOT%{_mandir}/man1
install etc/example.c*	$RPM_BUILD_ROOT%{_sysconfdir}/mplayer/mplayer.conf
install etc/codecs.c*	$RPM_BUILD_ROOT%{_sysconfdir}/mplayer/codecs.conf

gzip -9nf -r DOCS/{[A-Z]*,*.html}
gzip -9nf -r etc/example.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc DOCS/*.gz
%doc etc/*.gz
%lang(de) %doc DOCS/German
%lang(hu) %doc DOCS/Hungarian
%lang(pl) %doc DOCS/Polish
%lang(ru) %doc DOCS/Russian
%lang(es) %doc DOCS/Spanish
%dir %{_sysconfdir}/mplayer
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mplayer/*.conf
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
