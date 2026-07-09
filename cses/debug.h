// Pretty-printing dbg(...) macro. Only included when compiled with -DLOCAL.
#pragma once
#include <bits/stdc++.h>

namespace dbg_impl {
using namespace std;

template<class T, class = void> struct is_iterable : false_type {};
template<class T> struct is_iterable<T, void_t<decltype(begin(declval<T>())),
                                                decltype(end(declval<T>()))>> : true_type {};

inline void p(const string& s)      { cerr << '"' << s << '"'; }
inline void p(const char* s)        { cerr << '"' << s << '"'; }
inline void p(char c)               { cerr << '\'' << c << '\''; }
inline void p(bool b)               { cerr << (b ? "true" : "false"); }
template<class T>
inline auto p(const T& x) -> enable_if_t<!is_iterable<T>::value> { cerr << x; }

template<class A, class B> void p(const pair<A,B>& v);
template<class T> auto p(const T& v) -> enable_if_t<is_iterable<T>::value && !is_same<T,string>::value>;
template<class... Ts> void p(const tuple<Ts...>& t);

template<class A, class B> void p(const pair<A,B>& v) {
    cerr << '('; p(v.first); cerr << ", "; p(v.second); cerr << ')';
}
template<class T> auto p(const T& v) -> enable_if_t<is_iterable<T>::value && !is_same<T,string>::value> {
    cerr << '{'; bool first = true;
    for (const auto& x : v) { if (!first) cerr << ", "; p(x); first = false; }
    cerr << '}';
}
template<size_t I = 0, class... Ts>
inline typename enable_if<I == sizeof...(Ts)>::type p_tuple(const tuple<Ts...>&) {}
template<size_t I = 0, class... Ts>
inline typename enable_if<I < sizeof...(Ts)>::type p_tuple(const tuple<Ts...>& t) {
    if (I) cerr << ", "; p(get<I>(t)); p_tuple<I+1>(t);
}
template<class... Ts> void p(const tuple<Ts...>& t) { cerr << '('; p_tuple(t); cerr << ')'; }

inline void emit(const char*) {}
template<class T, class... Rest>
inline void emit(const char* names, const T& v, const Rest&... rest) {
    const char* comma = names;
    int depth = 0;
    while (*comma && !(*comma == ',' && depth == 0)) {
        if (*comma == '(' || *comma == '[' || *comma == '{' || *comma == '<') ++depth;
        else if (*comma == ')' || *comma == ']' || *comma == '}' || *comma == '>') --depth;
        ++comma;
    }
    cerr.write(names, comma - names);
    cerr << " = "; p(v);
    if (*comma) { cerr << ", "; emit(comma + 1, rest...); }
}
} // namespace dbg_impl

#define dbg(...) do { std::cerr << "[" << __LINE__ << "] "; \
                      dbg_impl::emit(#__VA_ARGS__, __VA_ARGS__); \
                      std::cerr << std::endl; } while (0)
