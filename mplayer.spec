%define	snap	20010331
Summary:	Yet another movie player for linux.
Summary(pl):	Jeszcze jeden odtwarzacz film�w dla linuxa.
Name:		mplayer
Version:	0.1
Release:	0.%{snap}
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://mplayer.sourceforge.net/snapshots/%{name}-main-current.tar.bz2
Source1:	%{name}.conf
Patch0:		%{name}-make.patch
URL:		http://mplayer.sourceforge.net/
Requires:	avi-codecs
BuildRequires:	SDL-devel >= 1.1.7
BuildRequires:	XFree86-devel >= 4.0.2
BuildRequires:	OpenGL-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86}

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
Odtwarzacz wideo dla linuxa. Wspierane formaty wej�ciowe: VCD
(VideoCD), MPEG1/2, RIFF AVI, ASF 1.0. Wspierane kodeki audio: PCM
(nieskompresowane), MPEG layer 2/3, AC3, aLaw, MS-GSM, Win32 ACM.
Wspierane kodeki wideo: MPEG 1 and MPEG 2, Win32 ICM (VfW), OpenDivX.
Wspierane urz�dzenia wyj�ciowe: Matrox G200/G400, X11 opcjonalnie z
rozszerzeniem SHM, X11 z rozszerzeniem Xvideo, renderer OpenGL, Matrox
G400 u�ywaj�c framebuffera, Voodoo2/3, SDL v1.1.7 itp.

%prep
%setup  -q -n main
%patch0 -p1

%build
%configure \
	--with-win32libdir="/usr/lib/win32" \
%ifarch i586 i686
	--enable-mmx \
	--enable-3dnow \
%ifarch i686
	--enable-sse \
%endif
%endif
	--enable-gl \
	--enable-dga \
	--enable-xv \
	--enable-vm \
	--enable-x11 \
	--enable-mga \
	--enable-xmga \
	--enable-fbdev \
	--enable-termcap
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}}

install mplayer		$RPM_BUILD_ROOT%{_bindir}
install DOCS/*.1	$RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1}	$RPM_BUILD_ROOT%{_sysconfdir}

gzip -9nf DOCS/{AUTHORS,CODECS,Change*,INSTALL,LIRC,MPla*,MTRR,Open*} \
	DOCS/{README,SPEED,TODO,VIDEOCARDS,example.conf,*.txt}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc DOCS/*.gz
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*.conf
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
