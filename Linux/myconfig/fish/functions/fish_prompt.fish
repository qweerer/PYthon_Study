bind \eg lazygit
# set -g __fish_git_prompt_show_informative_status 1
# 
# # Defined in /tmp/fish.hyt5lE/fish_prompt.fish @ line 2
# function fish_prompt --description 'Write out the prompt'
#     set -U last_pwd $PWD
#     set -l color_cwd
#     set -l suffix
#     switch "$USER"
#         case root toor
#             if set -q fish_color_cwd_root
#                 set color_cwd $fish_color_cwd_root
#             else
#                 set color_cwd $fish_color_cwd
#             end
#             set suffix '#'
#         case '*'
#             set color_cwd $fish_color_cwd
#             set suffix '➜'
#     end
# 
#     echo -n -s "["(set_color blue) "$USER" (set_color normal) @ (set_color brmagenta) (prompt_hostname) (set_color normal) '] ' # (set_color $color_cwd) (prompt_pwd) (set_color normal)
#     if set -q VIRTUAL_ENV
#         echo -n -s (set_color -b blue white) "(" (basename "$VIRTUAL_ENV") ")" (set_color normal)
#     end
#     echo -s (fish_git_prompt)
#     echo -n -s (set_color red) "$suffix "
# end

function fish_prompt --description 'Write out the prompt'
	set laststatus $status

    if set -l git_branch (command git symbolic-ref HEAD 2>/dev/null | string replace refs/heads/ '')
        set git_branch (set_color -o blue)"$git_branch"
        if command git diff-index --quiet HEAD --
            if set -l count (command git rev-list --count --left-right $upstream...HEAD 2>/dev/null)
                echo $count | read -l ahead behind
                if test "$ahead" -gt 0
                    set git_status "$git_status"(set_color red)⬆
                end
                if test "$behind" -gt 0
                    set git_status "$git_status"(set_color red)⬇
                end
            end
            for i in (git status --porcelain | string sub -l 2 | uniq)
                switch $i
                    case "."
                        set git_status "$git_status"(set_color green)✚
                    case " D"
                        set git_status "$git_status"(set_color red)✖
                    case "*M*"
                        set git_status "$git_status"(set_color purple)✱
                    case "*R*"
                        set git_status "$git_status"(set_color purple)➜
                    case "*U*"
                        set git_status "$git_status"(set_color brown)═
                    case "??"
                        set git_status "$git_status"(set_color red)≠
                end
            end
        else
            set git_status (set_color green)✱
        end
        set git_info "(git$git_status$git_branch"(set_color white)")"
    end

    set_color -b black
    printf '%s%s%s%s%s%s%s%s%s%s%s%s%s' (set_color -o white) '❰' (set_color green) $USER (set_color white) '❙' (set_color yellow) (echo $PWD | sed -e "s|^$HOME|~|") (set_color white) $git_info (set_color white) '❱' (set_color white)
    echo
    if test $laststatus -eq 0
        printf "%s✔%s≻%s " (set_color -o green) (set_color white) (set_color normal)
    else
        printf "%s✘%s≻%s " (set_color -o red) (set_color white) (set_color normal)
    end
end