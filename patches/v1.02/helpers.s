.syntax unified
.thumb
.section .text,"ax",%progbits

.equ APPUTIL_QUERY_STUB, 0x813877e0
.equ QUIT_GAME,          0x81a0fb34

.global lang_helper
.type lang_helper, %function
.thumb_func
lang_helper:
    /* Caller is load_configuration(): r4 = config base (install_info starts at r4+8).
       Replace displaced: ldr.w r3, [r4,#158]. */
    push {r5, r6, lr}
    sub sp, #4              /* keep 8-byte stack alignment for AppUtil */
    movs r5, #1             /* fallback raw language = English US */
    str r5, [sp, #0]
    movs r0, #1             /* SCE_SYSTEM_PARAM_ID_LANG */
    mov r1, sp
    blx APPUTIL_QUERY_STUB
    cmp r0, #0
    blt .Llang_fallback
    ldr r5, [sp, #0]
    cmp r5, #19
    bhi .Llang_fallback
    adr r6, .Llang_table
    ldrb r6, [r6, r5]
    b .Llang_store
.Llang_fallback:
    movs r6, #1             /* KeeperFX Lang_English */
.Llang_store:
    str.w r6, [r4, #158]    /* install_info.lang_id */
    mov r3, r6              /* recreate displaced load result for caller */
    add sp, #4
    pop {r5, r6, pc}

.align 2
.Llang_table:
    /* Vita: JP, EN-US, FR, ES, DE, IT, NL, PT-PT, RU, KO,
             ZH-T, ZH-S, FI, SV, DA, NO, PL, PT-BR, EN-GB, TR
       KFX : JP, EN,    FR, ES, DE, IT, NL, PT,    RU, KO,
             ZH-T, ZH-S, EN, SV, DA, NO, PL, PT,    EN,    EN */
    .byte 16,1,2,5,3,4,8,19,15,10,18,17,1,6,11,12,7,19,1,1

.align 2
.global quit_helper
.type quit_helper, %function
.thumb_func
quit_helper:
    /* r0 = PlayerInfo*, r1 = complete_quit. Match KeeperFX local semantics. */
    cbz r0, .Lquit_null
    push {r4, r5, r6, lr}
    mov r4, r0
    mov r5, r1
    ldrb r2, [r4, #0]
    bic r2, r2, #1          /* clear PlaF_Allocated */
    strb r2, [r4, #0]
    mov r0, r4
    bl 0x811114ac            /* is_my_player(player) */
    cbz r0, .Lquit_done
    movs r6, #1
.Lquit_pc:
    adr r3, .Lquit_pc
    ldr r2, .Lquit_delta
    add r3, r2              /* r3 = &quit_game, position independent */
    strb r6, [r3, #0]
    cbz r5, .Lquit_done
    strb r6, [r3, #20]      /* exit_keeper = quit_game + 0x14 */
.Lquit_done:
    pop {r4, r5, r6, pc}
.Lquit_null:
    bx lr
.align 2
.Lquit_delta:
    .word 0x006586AA  /* 0x81a0fb34 - 0x813b748a */
