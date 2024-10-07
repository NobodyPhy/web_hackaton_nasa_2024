/** @jsxImportSource @emotion/react */


import { Fragment, useContext, useEffect, useState } from "react"
import { ColorModeContext, EventLoopContext } from "/utils/context"
import { Event, getBackendURL, isTrue, refs } from "/utils/state"
import { HeartIcon as LucideHeartIcon, MenuIcon as LucideMenuIcon, WifiOffIcon as LucideWifiOffIcon } from "lucide-react"
import { keyframes } from "@emotion/react"
import { toast, Toaster } from "sonner"
import env from "/env.json"
import Script from "next/script"
import { Box as RadixThemesBox, Button as RadixThemesButton, Flex as RadixThemesFlex, Heading as RadixThemesHeading, Select as RadixThemesSelect, Text as RadixThemesText } from "@radix-ui/themes"
import NextHead from "next/head"



export function Toaster_9d6e054b03c6e5d1bea1c0a5576b4e6d () {
  const { resolvedColorMode } = useContext(ColorModeContext)


  refs['__toast'] = toast
  const [addEvents, connectErrors] = useContext(EventLoopContext);
  const toast_props = ({ ["description"] : ("Check if server is reachable at "+getBackendURL(env.EVENT).href), ["closeButton"] : true, ["duration"] : 120000, ["id"] : "websocket-error" });
  const [userDismissed, setUserDismissed] = useState(false);
  (useEffect(
() => {
    if ((connectErrors.length >= 2)) {
        if (!userDismissed) {
            toast.error(
                `Cannot connect to server: ${((connectErrors.length > 0) ? connectErrors[connectErrors.length - 1].message : '')}.`,
                {...toast_props, onDismiss: () => setUserDismissed(true)},
            )
        }
    } else {
        toast.dismiss("websocket-error");
        setUserDismissed(false);  // after reconnection reset dismissed state
    }
}
, [connectErrors]))

  return (
    <Toaster closeButton={false} expand={true} position={"bottom-right"} richColors={true} theme={resolvedColorMode}/>
  )
}

const pulse = keyframes`
    0% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
`


export function Div_24a2e81d0c5d3cb5b5f786fdef44e514 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    <div css={({ ["position"] : "fixed", ["width"] : "100vw", ["height"] : "0" })} title={("Connection Error: "+((connectErrors.length > 0) ? connectErrors[connectErrors.length - 1].message : ''))}>
  <Fragment_e521b13e556da291bcec5187a783ea81/>
</div>
  )
}

export function Fragment_e521b13e556da291bcec5187a783ea81 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    <Fragment>
  {isTrue((connectErrors.length > 0)) ? (
  <Fragment>
  <LucideWifiOffIcon css={({ ["color"] : "crimson", ["zIndex"] : 9999, ["position"] : "fixed", ["bottom"] : "33px", ["right"] : "33px", ["animation"] : (pulse+" 1s infinite") })} size={32}/>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

export default function Component() {

  return (
    <Fragment>
  <Fragment>
  <Div_24a2e81d0c5d3cb5b5f786fdef44e514/>
  <Toaster_9d6e054b03c6e5d1bea1c0a5576b4e6d/>
</Fragment>
  <Fragment>
  <Script src={"https://cdn.tailwindcss.com"} strategy={"afterInteractive"}/>
  <style suppressHydrationWarning>
  {"\n        @font-face {\n            font-family: 'LucideIcons';\n            src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');\n        }\n    "}
</style>
  <RadixThemesBox css={({ ["backgroundColor"] : "#F3F4F6", ["fontFamily"] : "system-ui, -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, \"Helvetica Neue\", Arial, \"Noto Sans\", sans-serif, \"Apple Color Emoji\", \"Segoe UI Emoji\", \"Segoe UI Symbol\", \"Noto Color Emoji\"", ["--default-font-family"] : "system-ui, -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, \"Helvetica Neue\", Arial, \"Noto Sans\", sans-serif, \"Apple Color Emoji\", \"Segoe UI Emoji\", \"Segoe UI Symbol\", \"Noto Color Emoji\"" })}>
  <RadixThemesBox css={({ ["backgroundColor"] : "#000000", ["boxShadow"] : "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)" })}>
  <RadixThemesBox css={({ ["@media screen and (min-width: 640px)"] : ({ ["max-width"] : "640px" }), ["@media screen and (min-width: 768px)"] : ({ ["max-width"] : "768px" }), ["@media screen and (min-width: 1024px)"] : ({ ["max-width"] : "1024px" }), ["@media screen and (min-width: 1280px)"] : ({ ["max-width"] : "1280px" }), ["@media screen and (min-width: 1536px)"] : ({ ["max-width"] : "1536px" }), ["width"] : "100%", ["marginLeft"] : "auto", ["marginRight"] : "auto", ["paddingLeft"] : "1rem", ["paddingRight"] : "1rem", ["paddingTop"] : "1rem", ["paddingBottom"] : "1rem" })}>
  <RadixThemesFlex css={({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "space-between" })}>
  <RadixThemesFlex css={({ ["display"] : "flex", ["alignItems"] : "center" })}>
  <img alt={"Company Logo"} css={({ ["height"] : "2.5rem", ["marginRight"] : "1rem" })} src={"Datito-sinfondo-(500x500).png"}/>
  <RadixThemesHeading as={"h1"} css={({ ["fontWeight"] : "700", ["fontSize"] : "1.5rem", ["lineHeight"] : "2rem", ["color"] : "#1F2937" })}>
  {"Dataether Agricultura"}
</RadixThemesHeading>
</RadixThemesFlex>
  <RadixThemesBox css={({ ["@media screen and (min-width: 0px)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 768px)"] : ({ ["display"] : "block" }) })}>
  <ul css={({ ["direction"] : "column", ["listStyleType"] : "none", ["display"] : "flex", ["columnGap"] : "1.5rem" })}>
  <li>
  <a css={({ ["transitionDuration"] : "300ms", ["&:hover"] : ({ ["color"] : "#de3e1c" }), ["color"] : "#ffffff", ["transitionProperty"] : "color, background-color, border-color, text-decoration-color, fill, stroke", ["transitionTimingFunction"] : "cubic-bezier(0.4, 0, 0.2, 1)" })} href={"#"}>
  {"Geodatos"}
</a>
</li>
  <li>
  <a css={({ ["transitionDuration"] : "300ms", ["&:hover"] : ({ ["color"] : "#de3e1c" }), ["color"] : "#ffffff", ["transitionProperty"] : "color, background-color, border-color, text-decoration-color, fill, stroke", ["transitionTimingFunction"] : "cubic-bezier(0.4, 0, 0.2, 1)" })} href={"#"}>
  {"Riesgos"}
</a>
</li>
  <li>
  <a css={({ ["transitionDuration"] : "300ms", ["&:hover"] : ({ ["color"] : "#de3e1c" }), ["color"] : "#ffffff", ["transitionProperty"] : "color, background-color, border-color, text-decoration-color, fill, stroke", ["transitionTimingFunction"] : "cubic-bezier(0.4, 0, 0.2, 1)" })} href={"#"}>
  {"Testimonios"}
</a>
</li>
  <LucideMenuIcon css={({ ["color"] : "var(--current-color)" })}/>
</ul>
</RadixThemesBox>
  <RadixThemesFlex css={({ ["display"] : "flex", ["alignItems"] : "center", ["columnGap"] : "1rem" })}>
  <button css={({ ["backgroundColor"] : "#45cead", ["transitionDuration"] : "300ms", ["&:hover"] : ({ ["background-color"] : "#2563EB" }), ["paddingLeft"] : "1rem", ["paddingRight"] : "1rem", ["paddingTop"] : "0.5rem", ["paddingBottom"] : "0.5rem", ["borderRadius"] : "0.25rem", ["color"] : "#ffffff", ["transitionProperty"] : "color, background-color, border-color, text-decoration-color, fill, stroke", ["transitionTimingFunction"] : "cubic-bezier(0.4, 0, 0.2, 1)", ["background"] : "center/cover url('Rectangulo - Rimau (1000 x 300 px).png')" })}>
  {"Rimau"}
</button>
  <RadixThemesBox css={({ ["@media screen and (min-width: 768px)"] : ({ ["display"] : "none" }) })}>
  <LucideMenuIcon css={({ ["height"] : "1.5rem", ["color"] : "#cc5298", ["width"] : "1.5rem" })}/>
</RadixThemesBox>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesBox>
</RadixThemesBox>
  <RadixThemesBox css={({ ["@media screen and (min-width: 640px)"] : ({ ["max-width"] : "640px" }), ["@media screen and (min-width: 768px)"] : ({ ["max-width"] : "768px" }), ["@media screen and (min-width: 1024px)"] : ({ ["max-width"] : "1024px" }), ["@media screen and (min-width: 1280px)"] : ({ ["max-width"] : "1280px" }), ["@media screen and (min-width: 1536px)"] : ({ ["max-width"] : "1536px" }), ["width"] : "100%", ["marginLeft"] : "auto", ["marginRight"] : "auto", ["paddingLeft"] : "1rem", ["paddingRight"] : "1rem", ["paddingTop"] : "2rem", ["paddingBottom"] : "2rem" })}>
  <RadixThemesFlex css={({ ["marginLeft"] : "-1rem", ["marginRight"] : "-1rem", ["display"] : "flex", ["flexWrap"] : "wrap" })}>
  <RadixThemesBox css={({ ["marginBottom"] : "2rem", ["paddingLeft"] : "1rem", ["paddingRight"] : "1rem", ["@media screen and (min-width: 0px)"] : ({ ["width"] : "100%" }), ["@media screen and (min-width: 768px)"] : ({ ["width"] : "33.333333%" }) })}>
  <RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["width"] : "100%" })} direction={"column"} gap={"3"}>
  <RadixThemesText align={"center"} as={"p"} color={"indigo"} css={({ ["width"] : "100%" })} weight={"bold"}>
  {"This is our region. :("}
</RadixThemesText>
  <img alt={"Visual element complementing the design"} css={({ ["height"] : "auto", ["borderRadius"] : "1rem", ["boxShadow"] : "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)", ["width"] : "100%" })} src={"ayacucho_final.jpg"}/>
</RadixThemesFlex>
</RadixThemesBox>
  <RadixThemesBox css={({ ["marginBottom"] : "2rem", ["marginTop"] : "4rem", ["paddingLeft"] : "1rem", ["paddingRight"] : "1rem", ["@media screen and (min-width: 0px)"] : ({ ["width"] : "100%" }), ["@media screen and (min-width: 768px)"] : ({ ["width"] : "33.333333%" }) })}>
  <RadixThemesBox css={({ ["display"] : "flex", ["flexDirection"] : "column", ["gap"] : "1rem", ["alignItems"] : "center" })}>
  <RadixThemesSelect.Root>
  <RadixThemesSelect.Trigger/>
  <RadixThemesSelect.Content>
  <RadixThemesSelect.Group>
  <RadixThemesSelect.Label>
  {"Distrito"}
</RadixThemesSelect.Label>
  <RadixThemesSelect.Item value={"Huamanga"}>
  {"Huamanga"}
</RadixThemesSelect.Item>
  <RadixThemesSelect.Item value={"Huanta"}>
  {"Huanta"}
</RadixThemesSelect.Item>
  <RadixThemesSelect.Item value={"La Mar"}>
  {"La Mar"}
</RadixThemesSelect.Item>
  <RadixThemesSelect.Item value={"Cangallo"}>
  {"Cangallo"}
</RadixThemesSelect.Item>
  <RadixThemesSelect.Item value={"Vilcashuam\u00e1n"}>
  {"Vilcashuam\u00e1n"}
</RadixThemesSelect.Item>
  <RadixThemesSelect.Item value={"V\u00edctor Fajardo"}>
  {"V\u00edctor Fajardo"}
</RadixThemesSelect.Item>
  <RadixThemesSelect.Item value={"Huanca Sancos"}>
  {"Huanca Sancos"}
</RadixThemesSelect.Item>
  <RadixThemesSelect.Item value={"Sucre"}>
  {"Sucre"}
</RadixThemesSelect.Item>
  <RadixThemesSelect.Item value={"Lucanas"}>
  {"Lucanas"}
</RadixThemesSelect.Item>
  <RadixThemesSelect.Item value={"Parinacochas"}>
  {"Parinacochas"}
</RadixThemesSelect.Item>
  <RadixThemesSelect.Item value={"Paucar del Sara Sara"}>
  {"Paucar del Sara Sara"}
</RadixThemesSelect.Item>
</RadixThemesSelect.Group>
</RadixThemesSelect.Content>
</RadixThemesSelect.Root>
  <RadixThemesButton color={"red"}>
  <LucideHeartIcon css={({ ["color"] : "var(--current-color)" })}/>
  {"Like"}
</RadixThemesButton>
  <RadixThemesButton color={"plum"}>
  <LucideHeartIcon css={({ ["color"] : "var(--current-color)" })}/>
  {"Ayacucho"}
</RadixThemesButton>
  <img align={"center"} alt={"Visual element complementing the design"} css={({ ["height"] : "auto", ["borderRadius"] : "1rem", ["boxShadow"] : "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)", ["width"] : "20%" })} src={"mapa peru ayacucho.png"}/>
</RadixThemesBox>
</RadixThemesBox>
  <RadixThemesBox css={({ ["marginBottom"] : "2rem", ["paddingLeft"] : "1rem", ["paddingRight"] : "1rem", ["@media screen and (min-width: 0px)"] : ({ ["width"] : "100%" }), ["@media screen and (min-width: 768px)"] : ({ ["width"] : "33.333333%" }), ["backgroundColor"] : "#3B82F6" })}>
  <RadixThemesBox css={({ ["display"] : "flex", ["flexDirection"] : "column", ["gap"] : "2rem" })}>
  <RadixThemesBox>
  <RadixThemesHeading as={"h2"} css={({ ["fontWeight"] : "700", ["marginBottom"] : "0.5rem", ["fontSize"] : "1.5rem", ["lineHeight"] : "2rem" })}>
  {"Here is your data"}
</RadixThemesHeading>
  <RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["width"] : "90%", ["height"] : "auto" })} direction={"column"} gap={"3"}>
  <RadixThemesButton css={({ ["width"] : "70%" })}>
  {"High temperature"}
</RadixThemesButton>
  <RadixThemesButton css={({ ["width"] : "70%" })}>
  {"Low precipitation"}
</RadixThemesButton>
</RadixThemesFlex>
</RadixThemesBox>
  <RadixThemesBox>
  <RadixThemesHeading as={"h2"} css={({ ["fontWeight"] : "700", ["marginBottom"] : "0.5rem", ["fontSize"] : "1.25rem", ["lineHeight"] : "1.75rem" })}>
  {"Here are the risks"}
</RadixThemesHeading>
  <RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["width"] : "90%", ["height"] : "auto" })} direction={"column"} gap={"3"}>
  <RadixThemesButton css={({ ["width"] : "70%" })}>
  {"Warning! Pathogen risk"}
</RadixThemesButton>
</RadixThemesFlex>
</RadixThemesBox>
  <RadixThemesBox>
  <RadixThemesHeading as={"h2"} css={({ ["fontWeight"] : "700", ["marginBottom"] : "0.5rem", ["fontSize"] : "1.25rem", ["lineHeight"] : "1.75rem" })}>
  {"We recommend"}
</RadixThemesHeading>
  <RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["width"] : "90%", ["height"] : "auto" })} direction={"column"} gap={"3"}>
  <RadixThemesBox css={({ ["width"] : "70%" })}>
  {"general recommendations"}
</RadixThemesBox>
</RadixThemesFlex>
</RadixThemesBox>
</RadixThemesBox>
</RadixThemesBox>
</RadixThemesFlex>
</RadixThemesBox>
</RadixThemesBox>
</Fragment>
  <NextHead>
  <title>
  {"Rxpython | Index"}
</title>
  <meta content={"favicon.ico"} property={"og:image"}/>
</NextHead>
</Fragment>
  )
}
