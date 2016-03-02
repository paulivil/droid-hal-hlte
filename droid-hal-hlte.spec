%define device hlte
%define vendor samsung

%define vendor_pretty Samsung
%define device_pretty Galaxy Note 3

%define installable_zip 1
%define straggler_files \
/selinux_version\
/service_contexts\
%{nil}

%include rpm/dhd/droid-hal-device.inc
